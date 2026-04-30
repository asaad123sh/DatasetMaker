import json
import os
import uuid
import random


def _entry_signature(entry):
    signature_payload = {
        "messages": entry.get("messages", []),
        "difficulty": entry.get("difficulty", ""),
        "tags": entry.get("tags", []),
        "safety_level": entry.get("safety_level", "safe"),
        "context": entry.get("context", ""),
    }
    return json.dumps(signature_payload, ensure_ascii=False, sort_keys=True)


def write_category_files(
    base_dir,
    category_name,
    generator_func,
    num_files=100,
    lines_per_file=30000,
    max_unique_attempts=8,
):
    category_dir = os.path.join(base_dir, category_name)
    os.makedirs(category_dir, exist_ok=True)
    
    total_generated = 0
    for file_idx in range(1, num_files + 1):
        filename = f"{category_name}_{file_idx:04d}.jsonl"
        filepath = os.path.join(category_dir, filename)
        seen_signatures = set()
        
        with open(filepath, "w", encoding="utf-8") as f:
            for _ in range(lines_per_file):
                entry = None
                signature = None

                for _attempt in range(max_unique_attempts):
                    candidate = generator_func()
                    signature = _entry_signature(candidate)
                    if signature not in seen_signatures:
                        entry = candidate
                        break

                if entry is None:
                    # Fallback keeps generation moving while preserving record uniqueness.
                    candidate = generator_func()
                    base_context = candidate.get("context", "Synthetic template generation")
                    candidate["context"] = f"{base_context} | variation:{uuid.uuid4().hex[:10]}"
                    signature = _entry_signature(candidate)
                    entry = candidate

                seen_signatures.add(signature)

                # Enforce required schema fields
                final_entry = {
                    "id": str(uuid.uuid4()),
                    "source": "synthetic_procedural",
                    "language": "en",
                    "category": category_name.lower(),
                    "messages": entry.get("messages", []),
                    "difficulty": entry.get("difficulty", random.choice(["easy", "medium"])),
                    "quality": "high",
                    "tags": entry.get("tags", []),
                    "safety_level": entry.get("safety_level", "safe"),
                    "context": entry.get("context", "Synthetic template generation")
                }
                f.write(json.dumps(final_entry, ensure_ascii=False) + "\n")
                total_generated += 1
                
        print(f"[{category_name}] Written {filepath} ({lines_per_file} lines)")
        
    print(f"Completed {category_name}: {total_generated} lines across {num_files} files.")
