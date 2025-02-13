from gradio_client import Client

client = Client("agents-course/beam_search_visualizer")
result = client.predict(
    n_beams=4,
    api_name="/change_num_return_sequences"
)
print(result)
