from starlette_admin.contrib.sqla import Admin, ModelView
 
from app.models import *
from app.database import engine, SessionLocal
 
admin = Admin(engine, title="Bilimdon Admin")
 
admin.add_view(ModelView(User))
admin.add_view(ModelView(Topic))
admin.add_view(ModelView(Question))
admin.add_view(ModelView(Option))
admin.add_view(ModelView(Game))
admin.add_view(ModelView(Participation))
admin.add_view(ModelView(Submission))
