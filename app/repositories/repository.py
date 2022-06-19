from app import db

class Repository:
    def create(self, model):
        db.session.add(model)
        db.session.commit()
        
        return model

    def update(self, model):
        db.session.commit()

        return model

    def delete(self, model):
        db.session.delete(model)
        db.session.commit()