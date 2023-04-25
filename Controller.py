class StructController:
    def __init__(self):
        self.adr_dev = 0
        self.adr_num_dev = 0
        self.napr_veter_adc = 0
        self.napr_veter_gr = 0
        self.napr_veter_sr = 0
        self.scor_veter_adc = 0
        self.himid_adc = 0
        self.adr_scor_veter = 0
        self.scor_veter_sr = 0
        self.himid = 0
        self.t_18b20 = 0
        self.k_scor_veter = 0
        self.cpar_himid = 0
        self.c_himid = 0
        self.k_upit = 0
        self.u_bat_d = 0


class Controller:
    def __init__(self, model):
        self.model = model
        self.struct = StructController()

