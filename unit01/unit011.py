from gradio_client import Client

client = Client("agents-course/decoding_visualizer")
result = client.predict(
    input_text="The Capital of France is",
    api_name="/get_beam_search_html"
)
print(result)
