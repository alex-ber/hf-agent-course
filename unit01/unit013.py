from gradio_client import Client

client = Client("agents-course/beam_search_visualizer")
result = client.predict(
    input_text="Conclusion: thanks a lot. That's all for today",
    number_steps=5,
    number_beams=4,
    length_penalty=1,
    num_return_sequences=3,
    api_name="/get_beam_search_html"
)
print(result)
