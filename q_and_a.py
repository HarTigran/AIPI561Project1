import fire
import torch


def tester(input_qn):
    from transformers import AutoTokenizer, AutoModelForQuestionAnswering

    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-cased-distilled-squad")

    model = AutoModelForQuestionAnswering.from_pretrained(
        "distilbert-base-cased-distilled-squad"
    )

    question, text = input_qn.split(",")

    inputs = tokenizer(question, text, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    answer_start_index = outputs.start_logits.argmax()
    answer_end_index = outputs.end_logits.argmax()

    predict_answer_tokens = inputs.input_ids[
        0, answer_start_index : answer_end_index + 1
    ]
    return tokenizer.decode(predict_answer_tokens)
    # return question, text


if __name__ == "__main__":
    fire.Fire(tester)
