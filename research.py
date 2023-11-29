from app import create_app, db
from app.Model.models import researchinterest,researchskills 

app = create_app()



@app.before_request
def initDB(*args, **kwargs):
    if app.got_first_request:
        db.create_all()
        if researchinterest.query.count() == 0:
            tags = ['Machine Learning','High Performance Computing', 'Bioinformatics', 'Software Engineering', 'Electronic Design Automation']
            for t in tags:
                db.session.add(researchinterest(name=t))
            db.session.commit()
        if researchskills.query.count() == 0:
            tags = ['Python','Java', 'C', 'C++', 'C#']
            for t in tags:
                db.session.add(researchskills(name=t))
            db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)