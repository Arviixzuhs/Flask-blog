from flask import Blueprint, render_template


class BlogController:
    def __init__(self):
        self.blog_bp = Blueprint("/", __name__)

        # Definición de rutas
        self.blog_bp.route("/", methods=["GET"])(self.get_main_page)
        self.blog_bp.route("/audio", methods=["GET"])(self.get_audio_page)
        self.blog_bp.route("/tictactoe", methods=["GET"])(self.get_tictactoe_page)
        self.blog_bp.route("/video", methods=["GET"])(self.get_video_page)
        self.blog_bp.route("/tictactoe", methods=["GET"])(self.get_tictactoe_page)
        self.blog_bp.route("/drag", methods=["GET"])(self.get_drag_and_drop_page)
        self.blog_bp.route("/gallery", methods=["GET"])(self.get_gallery_page)
        self.blog_bp.route("/list", methods=["GET"])(self.get_list_page)
        self.blog_bp.route("/admin", methods=["GET"])(self.get_manage_articles_page)

    def get_main_page(self):
        return render_template("index.html")

    def get_gallery_page(self):
        return render_template("gallery.html")

    def get_list_page(self):
        return render_template("list.html")

    def get_audio_page(self):
        return render_template("audio.html")

    def get_tictactoe_page(self):
        return render_template("tictactoe.html")

    def get_video_page(self):
        return render_template("video.html")

    def get_tic_tac_toe_page(self):
        return render_template("tictactoe.html")

    def get_drag_and_drop_page(self):
        return render_template("drag&drop.html")
    
    def get_manage_articles_page(self):
        return render_template("manageArticles.html")



# Instanciar el controlador
blog_controller = BlogController()
blog_bp = blog_controller.blog_bp
