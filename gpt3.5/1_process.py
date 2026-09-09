import json
import random

def transform_jsonl(input_file_path, output_file_path, system_prompt=None):
    entries = []
    with open(input_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            entry = json.loads(line)
            entries.append(entry)

    # 随机抽取100个条目
    sampled_entries = random.sample(entries, 100)

    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        for entry in sampled_entries:
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            user_message = {"role": "user", "content": entry["questions"]}
            assistant_message = {"role": "assistant", "content": entry["answers"]}
            messages.extend([user_message, assistant_message])
            result = {"messages": messages}
            json.dump(result, outfile, ensure_ascii=False)
            outfile.write('\n')

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='随机抽取 100 条问答，转换为微调 JSONL。')
    parser.add_argument('input_file', help='至少包含 100 条问答的 JSONL 文件')
    parser.add_argument('output_file', nargs='?', default='output.jsonl')
    parser.add_argument('--system-prompt', help='可选任务指令；推理时应保持一致')
    args = parser.parse_args()
    transform_jsonl(args.input_file, args.output_file, args.system_prompt)
