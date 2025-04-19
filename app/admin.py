from starlette_admin.contrib.sqla import Admin, ModelView
 
from app.models import User, Topic, Question, Option
from app.database import engine, SessionLocal
 
admin = Admin(engine, title="Bilimdon Admin")
 
admin.add_view(ModelView(User))
admin.add_view(ModelView(Topic))
admin.add_view(ModelView(Question))
admin.add_view(ModelView(Option))