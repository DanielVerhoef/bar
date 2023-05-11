"""
Main function to run the flask bar app from.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main() -> str:
    """
    Landing page for the bar.
    :return:
    """
    return "Hello world"

if __name__ == "__main__":
    app.run()

# if __name__ == "__main__":
#     main_jinja_path = template_folder_path / "main_jinja.html"  #
#
#     template_str = main_jinja_path.open().read()
#     User = namedtuple("User", "name lastname")
#     users = [User("Daniel", "Verhoef"), User("Sandra", "Venhoek"),
#              User("Harmen", "Kraayenbrink"), User("Marijke", "Wagenaar")]
#
#
#
#     Template(template_str).render(users=users,
#             products=["Wijn", "Bier", "Cola"])
#
