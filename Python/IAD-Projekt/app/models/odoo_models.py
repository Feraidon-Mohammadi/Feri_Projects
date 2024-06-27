from flask_restx import fields

""" alle benötigte Models struktur für Odoo """


def create_odoo_models(api):

    # diese schema wurde verwendet in GUI unter Models
    odoo_model_measur_number = api.model("Odoo_schema_measure_by_number", {
        "id": fields.Integer,
        "name": fields.String,
        "long_name": fields.String
    })

    # diese schema wurde verwendet in GUI unter Models
    odoo_model_measure_name = api.model("Odoo_schema_measure_by_name", {
        "id": fields.Integer,
        "name": fields.String,
    })

    # diese schema wurde verwendet in GUI unter Models
    odoo_model_partner = api.model("Odoo_schema_partner", {
        "id": fields.Integer,
        "name": fields.String,
        "email": fields.String,
        "active_education_plan_id": fields.List(fields.String),
    })

    odoo_model_measur = api.model("Odoo_schema_measur", {
        "id": fields.Integer,
        "name": fields.String,
        "long_name": fields.String,
        'location_id': fields.List(fields.String),
    })

    odoo_model_special = api.model("Odoo_schema_special", {
        "id": fields.Integer,
        "name": fields.String,
        "active_education_plan_id": fields.List(fields.String),
        "measure_number": fields.String
    })

    # verwendet für 3 models in ein response
    odoo_model_all = api.model("all_in_one_shema", {
        'nested_measur': fields.Nested(odoo_model_measur),
        'nested_special': fields.Nested(odoo_model_special),
        'nested_partner': fields.Nested(odoo_model_partner),
    })

    """ weitere schema models für die zukunft here ..."""

    # warnung!!!  untene fields nicht abberechen den line,
    # weil mit abbruch des line wird ein tuple ergelstelt
    # und tuple posictionen werden geändert, dann comt zu coflikt.
    return odoo_model_measur_number, odoo_model_partner, odoo_model_special, odoo_model_measur, odoo_model_measure_name, odoo_model_all
