import xmlrpc.client


class GetOdooData:

    def __init__(self):

        # Odoo database connection
        self.odoo_db_info = {
            'host': 'http://00.00.00.00',
            'port': "8069",
            'database': 'xxxxxxxx',
            'username': 'xxxxxxxxxxx',
            'password': 'xxxxxxxxxxxxx',
        }
        self.url = f"{self.odoo_db_info['host']}:{self.odoo_db_info['port']}"
        self.common = xmlrpc.client.ServerProxy("...objekt".format(self.url))

        self.uid = self.common.authenticate(
            self.odoo_db_info['database'],
            self.odoo_db_info['username'],
            self.odoo_db_info['password'], {}
        )
        self.models = xmlrpc.client.ServerProxy("...object".format(self.url))

    def get_data_by_model(self, model, domain, fields, limit):
        partner_ids = self.models.execute_kw(self.odoo_db_info['database'],
                                             self.uid,
                                             self.odoo_db_info['password'],
                                             model, 'search_read',
                                             domain, {'fields': fields, "limit": limit})
        return partner_ids

    def get_data_partner(self):
        domain = [[[]]]
        fields = ['id', 'vorname', 'nachname', 'forename', "measure_number"]  # Fields you want to retrieve
        limit = False
        partners = self.models.execute_kw(
            self.odoo_db_info['database'], self.uid, self.odoo_db_info['password'],
            'res_partner.partner', 'search_read', [domain], {'fields': fields, 'limit': limit}
        )
        #print(partners)
        return partners

    def get_data_measur(self):
        domain = [[[]]]  # If don't need specific filtering, leave the domain empty
        fields = ["id", "name", "long_name", "first_name", "phone",]  # Fields to retrieve

        limit = False
        measures = self.models.execute_kw(
            self.odoo_db_info['database'], self.uid, self.odoo_db_info['password'],
            'second_partner.model_name', 'search_read', [domain], {'fields': fields, 'limit': limit}
        )

        return measures

    def get_data_special(self):
        domain = [[[]]]
        fields = ["id", "name", "measure_name", 'display_name', 'date']  # addire mehr felder wenn existiert,

        limit = False
        special_days = self.models.execute_kw(
            self.odoo_db_info['database'], self.uid, self.odoo_db_info['password'],
            'third_partner.model_name', 'search_read', [domain], {'fields': fields, 'limit': limit}
        )

        return special_days


    """ to add data """
    def add_partner_data(self, data):

        """
        Create a new partner record in Odoo.

        :param data: A dictionary of the fields and their values for the new record.
        :return: The ID of the newly created record.
        """
        new_partner_id = self.models.execute_kw(
            self.odoo_db_info['database'], self.uid, self.odoo_db_info['password'],
            'res_partner.partner', 'create', [data]
        )
        return new_partner_id

    """ ------------ becarfull -------------"""
    def verify_partner_by_id_and_forename(self, partner_id, forename):
        partners = self.models.execute_kw(
            self.odoo_db_info['database'], self.uid, self.odoo_db_info['password'],
            'res.partner', 'search_read',
            [[['id', '=', partner_id], ['forename', '=', forename]]],
            {'fields': ['id', 'forename']}
        )
        partner_exists = bool(partners)
        partner_matched = any(partner for partner in partners if partner.get('forename') == forename)
        return partner_exists, partner_matched

    def delete_partner_data(self, partner_id):
        try:
            self.models.execute_kw(
                self.odoo_db_info['database'], self.uid, self.odoo_db_info['password'],
                # to remove some data or users instead of 'search_read'
                # should use ->'unlink' für security measur I changed it
                'res_partner.partner', 'search_read', [[partner_id]]
            )
            return True
        except Exception as e:
            print(e)
            return False