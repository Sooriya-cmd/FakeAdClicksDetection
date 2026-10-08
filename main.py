import argparse


def train_model():
    """Build, train, and evaluate the click classifier."""
    from configs.config import CFG
    from model.model import CLICK

    model = CLICK(CFG)
    model.load_data()
    model.build()
    model.train()
    model.load_test_data()
    model.evaluate()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Fake ad-click detection demo")
    parser.add_argument(
        "--train",
        action="store_true",
        help="train and evaluate the model instead of starting the local website",
    )
    arguments = parser.parse_args()

    if arguments.train:
        train_model()
    else:
        from web_app import create_app

        create_app().run(host="127.0.0.1", port=5000, debug=False)