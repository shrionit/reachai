import openai, json
from constants import OPENAI_KEY

openai.api_key = OPENAI_KEY


def write_to_file(file_path, content):
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Content successfully written to '{file_path}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")


context = [
    {
        "role": "system",
        "content": "Your are a ad generator for facebook ads you will use proper emojis first I will provide you the websites content in parts so you have to analyze the content and since it is a web scrapped content so there will be some reduntant information as well discard that and use what is needed to create a compelling ad. I will keep pasting the content in chunk in starting and when I will say generate ads only then you should generate ads.",
    }
]


def updateContext(whoSaid, what):
    c = {"role": whoSaid, "content": what}
    context.append(c)


def main():
    print("Enter 'quit' or 'exit' to terminate the program.")
    while True:
        q = input("\nYou: ")
        if q.lower() in ["quit", "exit"]:
            break
        if q == "_PRINT_CONTEXT":
            write_to_file("gptchat.json", json.dumps(context))
            continue
        updateContext("user", q)
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=context)
        content = response.choices[0].message.content
        updateContext("assistant", content)
        print("\nAI: ", content)


if __name__ == "__main__":
    main()
