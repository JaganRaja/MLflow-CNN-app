import io
import logging

def log_model_summary(model):
    with io.StringIO() as stream:
        model.summary(
            print_fn=lambda x: stream.write(f"{x}\n")                  #print_fn - helps to print the details
        )
        summary_str = stream.getvalue()
    return summary_str
