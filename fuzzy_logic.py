import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def hesapla_fuzzy(uyku_input, uyanma_input, gurultu_input, is_miktari_input, gun_input):
    uyku = ctrl.Antecedent(np.arange(0, 9.1, 0.1), 'uyku')
    uyanma = ctrl.Antecedent(np.arange(0, 31, 1), 'uyanma')
    gurultu = ctrl.Antecedent(np.arange(0, 101, 1), 'gurultu')
    is_miktari = ctrl.Antecedent(np.arange(0, 101, 1), 'is_miktari')
    gun = ctrl.Antecedent(np.arange(0, 3, 1), 'gun')

    alarm = ctrl.Consequent(np.arange(0, 101, 1), 'alarm')
    muzik = ctrl.Consequent(np.arange(0, 101, 1), 'muzik')

    uyku['cok_az'] = fuzz.trimf(uyku.universe, [0, 0, 2])
    uyku['az'] = fuzz.trimf(uyku.universe, [2, 3, 4])
    uyku['orta'] = fuzz.trimf(uyku.universe, [4, 5, 6])
    uyku['iyi'] = fuzz.trimf(uyku.universe, [6, 7, 8])
    uyku['mukemmel'] = fuzz.trimf(uyku.universe, [8, 9, 9])

    uyanma['cok_az'] = fuzz.trimf(uyanma.universe, [0, 0, 10])
    uyanma['az'] = fuzz.trimf(uyanma.universe, [10, 15, 20])
    uyanma['yeterli'] = fuzz.trimf(uyanma.universe, [20, 30, 30])

    gurultu['sessiz'] = fuzz.trimf(gurultu.universe, [0, 0, 40])
    gurultu['orta'] = fuzz.trimf(gurultu.universe, [40, 50, 60])
    gurultu['gurultulu'] = fuzz.trimf(gurultu.universe, [60, 100, 100])

    is_miktari['az'] = fuzz.trimf(is_miktari.universe, [0, 0, 40])
    is_miktari['orta'] = fuzz.trimf(is_miktari.universe, [40, 55, 70])
    is_miktari['cok'] = fuzz.trimf(is_miktari.universe, [70, 100, 100])

    gun['hafta_ici'] = fuzz.trimf(gun.universe, [0, 0, 0])
    gun['cumartesi'] = fuzz.trimf(gun.universe, [1, 1, 1])
    gun['pazar'] = fuzz.trimf(gun.universe, [2, 2, 2])

    alarm['yumusak'] = fuzz.trimf(alarm.universe, [0, 0, 30])
    alarm['orta'] = fuzz.trimf(alarm.universe, [30, 50, 70])
    alarm['sert'] = fuzz.trimf(alarm.universe, [70, 100, 100])

    muzik['rahatlatici'] = fuzz.trimf(muzik.universe, [0, 0, 30])
    muzik['normal'] = fuzz.trimf(muzik.universe, [30, 50, 70])
    muzik['enerjik'] = fuzz.trimf(muzik.universe, [70, 100, 100])

    rules = [
    ctrl.Rule(uyku['cok_az'] & uyanma['cok_az'] & gurultu['gurultulu'] & gun['hafta_ici'] & is_miktari['cok'], alarm['sert'] & muzik['enerjik']),
    ctrl.Rule(uyku['cok_az'] & uyanma['az'] & gurultu['orta'] & gun['hafta_ici'] & is_miktari['cok'], alarm['sert'] & muzik['normal']),
    ctrl.Rule(uyku['az'] & uyanma['az'] & gurultu['orta'] & gun['cumartesi'] & is_miktari['orta'], alarm['orta'] & muzik['normal']),
    ctrl.Rule(uyku['az'] & uyanma['yeterli'] & gurultu['sessiz'] & gun['pazar'] & is_miktari['az'], alarm['yumusak'] & muzik['rahatlatici']),
    ctrl.Rule(uyku['orta'] & uyanma['az'] & gurultu['orta'] & gun['hafta_ici'] & is_miktari['orta'], alarm['orta'] & muzik['normal']),
    ctrl.Rule(uyku['orta'] & uyanma['yeterli'] & gurultu['sessiz'] & gun['cumartesi'] & is_miktari['az'], alarm['yumusak'] & muzik['rahatlatici']),
    ctrl.Rule(uyku['iyi'] & uyanma['yeterli'] & gurultu['sessiz'] & gun['pazar'] & is_miktari['az'], alarm['yumusak'] & muzik['rahatlatici']),
    ctrl.Rule(uyku['mukemmel'] & uyanma['yeterli'] & gurultu['sessiz'] & gun['pazar'] & is_miktari['az'], alarm['yumusak'] & muzik['rahatlatici']),
    ctrl.Rule(uyku['mukemmel'] & uyanma['az'] & gurultu['orta'] & gun['hafta_ici'] & is_miktari['orta'], alarm['orta'] & muzik['normal']),
    ctrl.Rule(uyku['orta'] & uyanma['cok_az'] & gurultu['gurultulu'] & gun['hafta_ici'] & is_miktari['cok'], alarm['sert'] & muzik['enerjik']),
    ctrl.Rule(uyku['cok_az'] & uyanma['az'] & gurultu['orta'] & gun['pazar'] & is_miktari['cok'], alarm['sert'] & muzik['enerjik']),
    ctrl.Rule(uyku['az'] & uyanma['yeterli'] & gurultu['orta'] & gun['pazar'] & is_miktari['az'], alarm['yumusak'] & muzik['rahatlatici']),
    ctrl.Rule(uyku['az'] & uyanma['cok_az'] & gurultu['gurultulu'] & gun['cumartesi'] & is_miktari['orta'], alarm['sert'] & muzik['normal']),
    ctrl.Rule(uyku['orta'] & uyanma['az'] & gurultu['orta'] & gun['cumartesi'] & is_miktari['cok'], alarm['orta'] & muzik['enerjik']),
    ctrl.Rule(uyku['iyi'] & uyanma['az'] & gurultu['orta'] & gun['hafta_ici'] & is_miktari['az'], alarm['orta'] & muzik['normal']),
    ctrl.Rule(uyku['mukemmel'] & uyanma['yeterli'] & gurultu['gurultulu'] & gun['pazar'] & is_miktari['az'], alarm['orta'] & muzik['enerjik']),
    ctrl.Rule(uyku['orta'] & uyanma['cok_az'] & gurultu['sessiz'] & gun['cumartesi'] & is_miktari['az'], alarm['orta'] & muzik['rahatlatici']),
    ctrl.Rule(uyku['az'] & uyanma['az'] & gurultu['orta'] & gun['hafta_ici'] & is_miktari['az'], alarm['orta'] & muzik['normal']),
    ctrl.Rule(uyku['iyi'] & uyanma['yeterli'] & gurultu['orta'] & gun['cumartesi'] & is_miktari['orta'], alarm['yumusak'] & muzik['normal']),
    ctrl.Rule(uyku['mukemmel'] & uyanma['yeterli'] & gurultu['sessiz'] & gun['hafta_ici'] & is_miktari['cok'], alarm['orta'] & muzik['normal']),
    ctrl.Rule(uyku['mukemmel'] & uyanma['yeterli'] & gurultu['sessiz'] & gun['cumartesi'] & is_miktari['orta'], alarm['yumusak'] & muzik['rahatlatici']),
    ctrl.Rule(uyku['iyi'] & uyanma['az'] & gurultu['orta'] & gun['pazar'] & is_miktari['az'], alarm['orta'] & muzik['rahatlatici']),
    ctrl.Rule(uyku['az'] & uyanma['cok_az'] & gurultu['orta'] & gun['hafta_ici'] & is_miktari['orta'], alarm['sert'] & muzik['normal']),
    ctrl.Rule(uyku['cok_az'] & uyanma['cok_az'] & gurultu['orta'] & gun['hafta_ici'] & is_miktari['orta'], alarm['sert'] & muzik['enerjik']),
    ctrl.Rule(uyku['mukemmel'] & uyanma['yeterli'] & gurultu['sessiz'] & gun['pazar'] & is_miktari['orta'], alarm['yumusak'] & muzik['rahatlatici']),
    ctrl.Rule(uyku['iyi'] & uyanma['az'] & gurultu['gurultulu'] & gun['hafta_ici'] & is_miktari['orta'], alarm['sert'] & muzik['enerjik']),
    ctrl.Rule(uyku['az'] & uyanma['az'] & gurultu['orta'] & gun['cumartesi'] & is_miktari['az'], alarm['orta'] & muzik['normal']),
    ctrl.Rule(uyku['orta'] & uyanma['az'] & gurultu['orta'] & gun['pazar'] & is_miktari['az'], alarm['orta'] & muzik['normal']),
    ctrl.Rule(uyku['az'] & uyanma['az'] & gurultu['sessiz'] & gun['cumartesi'] & is_miktari['orta'], alarm['orta'] & muzik['normal']),
    ctrl.Rule(uyku['cok_az'] & uyanma['az'] & gurultu['orta'] & gun['cumartesi'] & is_miktari['orta'], alarm['sert'] & muzik['normal']),
    ctrl.Rule(uyku['iyi'] & uyanma['yeterli'] & gurultu['sessiz'] & gun['hafta_ici'] & is_miktari['az'], alarm['yumusak'] & muzik['rahatlatici']),
    ctrl.Rule(uyku['az'] & uyanma['yeterli'] & gurultu['sessiz'] & gun['hafta_ici'] & is_miktari['az'], alarm['orta'] & muzik['normal']),
    ctrl.Rule(uyku['orta'] & uyanma['az'] & gurultu['orta'] & gun['hafta_ici'] & is_miktari['az'], alarm['orta'] & muzik['normal']),
    ctrl.Rule(uyku['mukemmel'] & uyanma['az'] & gurultu['sessiz'] & gun['cumartesi'] & is_miktari['az'], alarm['orta'] & muzik['rahatlatici']),
    ctrl.Rule(uyku['az'] & uyanma['cok_az'] & gurultu['gurultulu'] & gun['hafta_ici'] & is_miktari['cok'], alarm['sert'] & muzik['enerjik']),
    ctrl.Rule(uyku['az'] & uyanma['az'] & gurultu['gurultulu'] & gun['cumartesi'] & is_miktari['cok'], alarm['sert'] & muzik['enerjik']),
    ctrl.Rule(uyku['cok_az'] & uyanma['az'] & gurultu['gurultulu'] & gun['pazar'] & is_miktari['orta'], alarm['sert'] & muzik['normal']),
    ctrl.Rule(uyku['orta'] & uyanma['yeterli'] & gurultu['orta'] & gun['hafta_ici'] & is_miktari['orta'], alarm['orta'] & muzik['normal']),
    

    
]


    alarm_muzik_ctrl = ctrl.ControlSystem(kurallar)
    alarm_muzik_sim = ctrl.ControlSystemSimulation(alarm_muzik_ctrl)

    alarm_muzik_sim.input['uyku'] = uyku_input
    alarm_muzik_sim.input['uyanma'] = uyanma_input
    alarm_muzik_sim.input['gurultu'] = gurultu_input
    alarm_muzik_sim.input['is_miktari'] = is_miktari_input
    alarm_muzik_sim.input['gun'] = gun_input

    alarm_muzik_sim.compute()

    return alarm_muzik_sim.output['alarm'], alarm_muzik_sim.output['muzik']
