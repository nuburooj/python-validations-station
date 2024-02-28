from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Station(db.Model):
    __tablename__ = "stations"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    city = db.Column(db.String(80))

    def __repr__(self):
        return f"<Station {self.name}>"
    

    #Station Validation
    @validates('name')
    def validate_name(self, key, name):
        if len(name) >= 3:
            return name
        else:
            raise ValueError("Station name must be atleast 3 characters long")


class Platform(db.Model):
    __tablename__ = "platforms"

    id = db.Column(db.Integer, primary_key=True)
    platform_num = db.Column(db.Integer, unique=True)
    station_id = db.Column(db.Integer, db.ForeignKey("stations.id"))

    def __repr__(self):
        return f"<Platform {self.name}>"
    
    #Platform validation
    @validates('platform_num')
    def validate_platform_num(self, key, platform_num):
        if isinstance(platform_num, int) <= platform_num <= 20:
            return platform_num
        else:
            raise ValueError("Platform none must be an integer between 1 and 20")


class Train(db.Model):
    __tablename__ = "trains"

    id = db.Column(db.Integer, primary_key=True)
    train_num = db.Column(db.String)
    service_type = db.Column(db.String)
    origin = db.Column(db.String)
    destination = db.Column(db.String)

    def __repr__(self):
        return f"<Train {self.name}>"
   
    #Train Validations
    @validates('origin')
    def validate_origin(self, key, origin):
        if 3 <= len(origin) <= 24:
            return origin
        else:
            raise ValueError("Origin must be a sring between 3 and 24 characters.")
        
    @validates('destination')
    def validate_destination(self, key, destination):
        if 3 <= len(destination) <= 24:
            return destination
        else:
            raise ValueError("Destination must be an integer between 3 and 24 characters.")

    @validates('service_type')
    def validate_service_type(self, key, service_type):
        if service_type == "express" or service_type == "local":
            return service_type
        else:
            raise ValueError("Service type must be either local or express.")
class Assignment(db.Model):
    __tablename__ = "assignments"

    id = db.Column(db.Integer, primary_key=True)
    arrival_time = db.Column(db.DateTime)
    departure_time = db.Column(db.DateTime)
    train_id = db.Column(db.Integer, db.ForeignKey("trains.id"))
    platform_id = db.Column(db.Integer, db.ForeignKey("platforms.id"))

    def __repr__(self):
        return f"<Assignment Train No: {self.train.train_num} Platform: {self.platform.platform_num}>"

@validates('Assignment')
def validate_arrival