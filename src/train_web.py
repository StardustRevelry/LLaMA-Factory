from llmtuner import create_ui
import sys


def main(port=7860):
    demo = create_ui()
    demo.queue()
    demo.launch(server_name="0.0.0.0", server_port=port, share=False, inbrowser=True)


if __name__ == "__main__":
    port = None
    for arg in sys.argv[1:]:
        if arg.startswith("--port"):
            port = int(arg.split("=")[1])
    main(port)
