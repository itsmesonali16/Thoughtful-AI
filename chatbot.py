responses = {
    "What is Thoughtful AI?": "Thoughtful AI is a company dedicated to building intuitive and ethical AI solutions for businesses.",
    "What services do you offer?": "We provide AI consulting, custom AI development, and pre-built AI solutions tailored to your needs.",
    "How can I contact support?": "You can reach us at support@thoughtfulai.com or call our helpline at +1-800-123-4567.",
    "What industries do you serve?": "We work with clients in healthcare, finance, retail, and more.",
    "Do you offer free trials?": "Yes, we offer free trials for selected products. Contact us for more details."
}

def get_response(user_input):
    user_input = user_input.strip().lower()
    for question, answer in responses.items():
        if user_input in question.lower():
            return answer
    return "I'm sorry, I couldn't find an answer to your question. Could you rephrase it or ask about something specific to Thoughtful AI?"


def chat_with_ai(user_input):
    return get_response(user_input)

# Launch Gradio interface
interface = gr.Interface(
    fn=chat_with_ai,
    inputs="text",
    outputs="text",
    title="Thoughtful AI - Customer Support",
    description="Ask any questions about Thoughtful AI's products or services!",
    examples=[
        "What is Thoughtful AI?",
        "How can I contact support?",
        "Do you offer free trials?",
    ]
)

# Run the app
if __name__ == "__main__":
    interface.launch()   
