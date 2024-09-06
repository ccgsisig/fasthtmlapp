from fasthtml.common import *

app = FastHTML()

@app.route("/", methods=['GET'])
def home():
    page = Html(
        Head(Title('Sisi'), Meta(charset='utf-8')),
        Body(Div(H1('Welcome to Sisi's Blog!'), 
                 A('Logo', href='https://sampleblog.com'),
                 Img(src='https://placehold.it/300x300', alt='Logo'),))
    )
    return page

@app.route("/", methods=['POST'])
def post_home():
    return 'POST request recieved! Yaaay!'