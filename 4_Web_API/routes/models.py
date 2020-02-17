'''
Module qui définie la connexion à la base de données en utilisant 
la librarie Pony comme ORM (object-relational mapper)
Ref: https://docs.ponyorm.org/queries.html
'''
from pony.orm import Database, Required, Optional, PrimaryKey

db = Database()

# Déckaration des entities reliées aux objets de la base de donnée: messier, cladwell et Herschel400 dans notre cas 
class Messier(db.Entity):
        '''
        Table de messier
        '''
        Messier_number  = PrimaryKey(str)           
        NGC_IC_designation = Required(str, unique=True)                    
        object_type =  Required(str)                          
        Common_name  = Optional(str)                       
        Constelation_name_abrv =  Required(str)              
        Constellation_Latin  = Required(str)                 
        Constellation_FR  = Optional(str)     
        Constellation_EN  = Optional(str)                     
        Hubble_morphological_type  = Optional(str)            
        Discoverer  = Optional(str) 
        Year  = Optional(str) 
        Season = Optional(str) 
        Right_Ascension  = Required(str) 
        Declinaison  = Required(str) 
        Distance_light_year = Optional(str)
        Size = Optional(str)
        major_axis = Optional(str)
        minor_axis = Optional(str)
        major__axis_position_angle = Optional(str)
        Apparent_magnitude_jbcurtin_gitHub = Optional(str)
        Magnitude = Required(str) 
        B_Apparent_Magnitude = Optional(str)
        V_Apparent_Magnitude = Optional(str)
        J_Apparent_Magnitude = Optional(str)
        H_Apparent_Magnitude = Optional(str)
        K_Apparent_Magnitude = Optional(str)
        Mean_surface_brigthness = Optional(str)
        Center_star_name = Optional(str)
        center_star_U_maghitude = Optional(str)
        center_star_B_maghitude = Optional(str)
        center_star_V_maghitude = Optional(str)
        Image1 = Optional(str)
        Image2 = Optional(str)
        image_jbcurtin_gitHub = Optional(str)
        NGC_number = Optional(str)
        Identifiers = Optional(str)
        NED_notes = Optional(str)
        OpenNGC_notes = Optional(str)

class Caldwell(db.Entity):
        '''
        Table de caldwell
        '''
        Caldwell_number = PrimaryKey(str)
        NGC_IC_designation = Required(str, unique=True) 
        object_type = Required(str)
        Common_names = Optional(str)
        Constelation_name_abrv = Required(str)
        Constellation_Latin = Required(str)
        Hubble_morphological_type = Optional(str)
        Right_Ascension = Optional(str)
        Declinaison = Optional(str)
        Size = Optional(str)
        major_axis = Optional(str)
        minor_axis  = Optional(str)
        major__axis_position_angle = Optional(str)
        B_Apparent_Magnitude = Optional(str)
        V_Apparent_Magnitude = Optional(str)
        J_Apparent_Magnitude = Optional(str)
        H_Apparent_Magnitude = Optional(str)
        K_Apparent_Magnitude = Optional(str)
        Mean_surface_brigthness = Optional(str)
        Center_star_name = Optional(str)
        center_star_U_maghitude = Optional(str)
        center_star_B_maghitude = Optional(str)
        center_star_V_maghitude = Optional(str)
        NGC_number = Optional(str)  
        IC_number  = Optional(str)
        Identifiers = Optional(str)
        NED_notes = Optional(str)
        OpenNGC_notes = Optional(str)

class Herschel400(db.Entity):
        '''
        Table de Herschel400
        '''
        NGC_designation = PrimaryKey(str)
        object_type = Required(str)
        Common_names = Optional(str)
        Constelation_name_abrv = Required(str)
        Constellation_Latin = Required(str)
        Hubble_morphological_type = Optional(str)
        Right_Ascension = Optional(str)
        Declinaison = Optional(str)
        major_axis = Optional(str)
        minor_axis = Optional(str)
        major__axis_position_angle = Optional(str)
        Magnitude = Optional(str)
        B_Apparent_Magnitude = Optional(str)
        V_Apparent_Magnitude = Optional(str)
        J_Apparent_Magnitude = Optional(str)
        H_Apparent_Magnitude = Optional(str)
        K_Apparent_Magnitude = Optional(str)
        Mean_surface_brigthness = Optional(str)
        Center_star_name = Optional(str)
        center_star_U_maghitude = Optional(str)
        center_star_B_maghitude = Optional(str)
        center_star_V_maghitude = Optional(str)
        Messier_number = Optional(str)
        Caldwell_number = Optional(str)
        NGC_number = Optional(str)
        IC_number = Optional(str)
        Identifiers = Optional(str)
        NED_notes = Optional(str)
        OpenNGC_notes = Optional(str)

 

#@db_session
def select_object(db, table, object):
    print("test")
    #p = Messier["M1"]
    #print (db.Messier.select())
    return db.select("select * from Messier where Messier_number = 'M1'")
    #return select(o for o in table
     #           if o.Messier_number == object)