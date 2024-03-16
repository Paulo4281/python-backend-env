# ROUTES
from src.routes.view_routes import view_routes
from src.routes.user_routes import user_routes
from src.routes.book_routes import book_routes
from src.routes.category_routes import category_routes
from src.routes.review_routes import review_routes
from src.routes.author_routes import author_routes

# Namespaces
from src.docs.modules.book.category_docs import api as category_namespace
from src.docs.modules.book.book_docs import api as book_namespace
from src.docs.modules.book.author_docs import api as author_namespace
from src.docs.modules.user.user_docs import api as user_namespace
from src.docs.modules.book.review_docs import api as review_namespace