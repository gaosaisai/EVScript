from InjectSignal_structParser import *

TC_CLEAR = [
    #Ricardo:Done
    (2,   SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'OfbChrgPrflUpdate_B_Rq':1}),
    (0.2, SEND_MSG,  GWM_HPCM_i_FrP14_CAN_ID, send_GWM_HPCM_i_FrP14, {'OfbChrgSetSync_D_Stat':0x1}),

    # Clear Saved location list
    (0.5, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,   send_Saved_Charge_Locat_HS3,   {'ChrgLocId_D_Sav':0, 'ChrgLocSaved_B_Dsply':0x1}),
    (0.5, SEND_MSG, ChargeSettings_HS3_CAN_ID,       send_ChargeSettings_HS3,       {'ChrgProgIdSaved_D_Stat':0}),
    # Clear Unsaved location
    (0.5, SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':0}),
        (2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'OfbChrgPrflUpdate_B_Rq':0}),
    (4, SEND_MSG,  GWM_HPCM_i_FrP14_CAN_ID, send_GWM_HPCM_i_FrP14, {'OfbChrgSetSync_D_Stat':0x2}),
]

# Add 3 saved locations
TC_SAVED_3 = [
    #Ricardo:Done
    (2,   SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'OfbChrgPrflUpdate_B_Rq':1}),
    (0.2, SEND_MSG,  GWM_HPCM_i_FrP14_CAN_ID, send_GWM_HPCM_i_FrP14, {'OfbChrgSetSync_D_Stat':0x1}),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':1, 'latitude':41.883627, 'longitude':-87.634747, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':1, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':2, 'latitude':41.881550, 'longitude':-87.636116, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':2, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':3, 'latitude':41.880926, 'longitude':-87.636030, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':3, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'OfbChrgPrflUpdate_B_Rq':0}),
    (4, SEND_MSG,  GWM_HPCM_i_FrP14_CAN_ID, send_GWM_HPCM_i_FrP14, {'OfbChrgSetSync_D_Stat':0x2}),
]

# Add 1 saved locations
TC_SAVED_1 = [
    #Ricardo:Done
    (2,   SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'OfbChrgPrflUpdate_B_Rq':1}),
    (0.2, SEND_MSG,  GWM_HPCM_i_FrP14_CAN_ID, send_GWM_HPCM_i_FrP14, {'OfbChrgSetSync_D_Stat':0x1}),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':1, 'latitude':41.883627, 'longitude':-87.634747, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':1, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'OfbChrgPrflUpdate_B_Rq':0}),
    (4, SEND_MSG,  GWM_HPCM_i_FrP14_CAN_ID, send_GWM_HPCM_i_FrP14, {'OfbChrgSetSync_D_Stat':0x2}),
]

# Add 4 saved locations
TC_SAVED_4 = [
    #Ricardo:Done
    (2,   SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'OfbChrgPrflUpdate_B_Rq':1}),
    (0.2, SEND_MSG,  GWM_HPCM_i_FrP14_CAN_ID, send_GWM_HPCM_i_FrP14, {'OfbChrgSetSync_D_Stat':0x1}),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':1, 'latitude':41.883627, 'longitude':-87.634747, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':1, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':2, 'latitude':41.881550, 'longitude':-87.636116, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':2, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':3, 'latitude':41.880926, 'longitude':-87.636030, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':3, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':4, 'latitude':41.879020, 'longitude':-87.634493, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':4, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'OfbChrgPrflUpdate_B_Rq':0}),
    (4, SEND_MSG,  GWM_HPCM_i_FrP14_CAN_ID, send_GWM_HPCM_i_FrP14, {'OfbChrgSetSync_D_Stat':0x2}),
]


# Add 10 saved locations
TC_9BD = [
    #Ricardo:Done
    (2,   SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'OfbChrgPrflUpdate_B_Rq':1}),
    (0.2, SEND_MSG,  GWM_HPCM_i_FrP14_CAN_ID, send_GWM_HPCM_i_FrP14, {'OfbChrgSetSync_D_Stat':0x1}),
    
     # Clear Saved location list
    (0.5, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,   send_Saved_Charge_Locat_HS3,   {'ChrgLocId_D_Sav':0, 'ChrgLocSaved_B_Dsply':0x1}),
    (0.5, SEND_MSG, ChargeSettings_HS3_CAN_ID,       send_ChargeSettings_HS3,       {'ChrgProgIdSaved_D_Stat':0}),
    # Clear Unsaved location
    (0.5, SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':0}),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':1, 'latitude':41.883627, 'longitude':-87.634747, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':1, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':2, 'latitude':41.881550, 'longitude':-87.636116, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':2, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':3, 'latitude':41.880926, 'longitude':-87.636030, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':3, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':4, 'latitude':41.879020, 'longitude':-87.634493, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':4, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':5, 'latitude':41.877475, 'longitude':-87.634156, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':5, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':6, 'latitude':41.884916, 'longitude':-87.623124, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':6, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':7, 'latitude':41.886393, 'longitude':-87.620037, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':7, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':8, 'latitude':41.893823, 'longitude':-87.61955, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':8, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':9, 'latitude':41.893795, 'longitude':-87.620766, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':9, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':10, 'latitude':41.883001, 'longitude':-87.634253, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':10, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'OfbChrgPrflUpdate_B_Rq':0}),
    (4, SEND_MSG,  GWM_HPCM_i_FrP14_CAN_ID, send_GWM_HPCM_i_FrP14, {'OfbChrgSetSync_D_Stat':0x2}),
]

# Add 5 unsaved and 5 saved locations
TC_SET = [
    #Ricardo:Done
    (2,   SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'OfbChrgPrflUpdate_B_Rq':1}),
    (0.2, SEND_MSG,  GWM_HPCM_i_FrP14_CAN_ID, send_GWM_HPCM_i_FrP14, {'OfbChrgSetSync_D_Stat':0x1}),
    
     # Clear Saved location list
    (0.5, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,   send_Saved_Charge_Locat_HS3,   {'ChrgLocId_D_Sav':0, 'ChrgLocSaved_B_Dsply':0x1}),
    (0.5, SEND_MSG, ChargeSettings_HS3_CAN_ID,       send_ChargeSettings_HS3,       {'ChrgProgIdSaved_D_Stat':0}),
    # Clear Unsaved location
    (0.5, SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':0}),
    
     # Add 5 UNSAVED location
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':1, 'latitude':41.883627, 'longitude':-87.634747}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':1}),
    
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':2, 'latitude':41.883627, 'longitude':-87.634747}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':1}),
    
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':3, 'latitude':41.883627, 'longitude':-87.634747}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':1}),
    
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':4, 'latitude':41.883627, 'longitude':-87.634747}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':1}),
    
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':5, 'latitude':41.883627, 'longitude':-87.634747}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':1}),
    
    
    # Add 5 Saved locations
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':1, 'latitude':41.883627, 'longitude':-87.634747, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':1, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':2, 'latitude':41.881550, 'longitude':-87.636116, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':2, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':3, 'latitude':41.880926, 'longitude':-87.636030, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':3, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':4, 'latitude':41.879020, 'longitude':-87.634493, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':4, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':5, 'latitude':41.877475, 'longitude':-87.634156, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':5, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'OfbChrgPrflUpdate_B_Rq':0}),
    (4, SEND_MSG,  GWM_HPCM_i_FrP14_CAN_ID, send_GWM_HPCM_i_FrP14, {'OfbChrgSetSync_D_Stat':0x2}),
]

# Add 6 unsaved and 6 saved locations
TC_SET2 = [
    #Ricardo:Done
    (2,   SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'OfbChrgPrflUpdate_B_Rq':1}),
    (0.2, SEND_MSG,  GWM_HPCM_i_FrP14_CAN_ID, send_GWM_HPCM_i_FrP14, {'OfbChrgSetSync_D_Stat':0x1}),
    
     # Clear Saved location list
    (0.5, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,   send_Saved_Charge_Locat_HS3,   {'ChrgLocId_D_Sav':0, 'ChrgLocSaved_B_Dsply':0x1}),
    (0.5, SEND_MSG, ChargeSettings_HS3_CAN_ID,       send_ChargeSettings_HS3,       {'ChrgProgIdSaved_D_Stat':0}),
    # Clear Unsaved location
    (0.5, SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':0}),
    
     # Add 6 UNSAVED location
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':1, 'latitude':41.883627, 'longitude':-87.634747}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':1}),
    
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':2, 'latitude':41.881550, 'longitude':-87.636116}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':1}),
    
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':3, 'latitude':41.880926, 'longitude':-87.636030}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':1}),
    
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':4, 'latitude':41.879020, 'longitude':-87.634493}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':1}),
    
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':5, 'latitude':41.877475, 'longitude':-87.634156}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':1}),
    
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':6, 'latitude':41.884916, 'longitude':-87.623124}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':1}),
    
    
    # Add 6 Saved locations
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':1, 'latitude':41.883627, 'longitude':-87.634747, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':1, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':2, 'latitude':41.881550, 'longitude':-87.636116, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':2, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':3, 'latitude':41.880926, 'longitude':-87.636030, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':3, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':4, 'latitude':41.879020, 'longitude':-87.634493, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':4, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':5, 'latitude':41.877475, 'longitude':-87.634156, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':5, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (0.2, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,  send_Saved_Charge_Locat_HS3,    {'ChrgLocId_D_Sav':6, 'latitude':41.884916, 'longitude':-87.623124, 'ChrgLocSaved_B_Dsply':0x1}, 100),
    (0.2, SEND_MSG, ChargeSettings_HS3_CAN_ID,      send_ChargeSettings_HS3,        {'ChrgProgIdSaved_D_Stat':6, 'ChrgToPcWkdySav_D_Stat':0, 'ChrgPrflWkdy_No_Actl':0, 'ChrgToPcWkndSav_D_Stat':0, 'ChrgPrflWknd_No_Actl':0, 'ChrgNowEnbl_B_Saved':0, 'ChrgLocIdCurnt_D_Sav':0}, 100),
    
    (2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'OfbChrgPrflUpdate_B_Rq':0}),
    (4, SEND_MSG,  GWM_HPCM_i_FrP14_CAN_ID, send_GWM_HPCM_i_FrP14, {'OfbChrgSetSync_D_Stat':0x2}),
]

# Add 1 Unsaved location to the list
TC_UNSAVED_1 = [
    #Ricardo:Done
    (2,   SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'OfbChrgPrflUpdate_B_Rq':1}),
    (0.2, SEND_MSG,  GWM_HPCM_i_FrP14_CAN_ID, send_GWM_HPCM_i_FrP14, {'OfbChrgSetSync_D_Stat':0x1}),
    # Clear Saved location list
    (0.5, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,   send_Saved_Charge_Locat_HS3,   {'ChrgLocId_D_Sav':0, 'ChrgLocSaved_B_Dsply':0x1}),
    (0.5, SEND_MSG, ChargeSettings_HS3_CAN_ID,       send_ChargeSettings_HS3,       {'ChrgProgIdSaved_D_Stat':0}),
    # Clear Unsaved location
    (0.5, SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':0}),
    
     # Add 1 UNSAVED location
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':5, 'latitude':41.883627, 'longitude':-87.634747}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':5}),
    (2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'OfbChrgPrflUpdate_B_Rq':0}),
    (4, SEND_MSG,  GWM_HPCM_i_FrP14_CAN_ID, send_GWM_HPCM_i_FrP14, {'OfbChrgSetSync_D_Stat':0x2}),
]

# Add 10 different unsaved loca
TC_SET3 = [
    #Ricardo:Done
    (2,   SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'OfbChrgPrflUpdate_B_Rq':1}),
    (0.2, SEND_MSG,  GWM_HPCM_i_FrP14_CAN_ID, send_GWM_HPCM_i_FrP14, {'OfbChrgSetSync_D_Stat':0x1}),
    
     # Clear Saved location list
    (0.5, SEND_MSG, Saved_Charge_Locat_HS3_CAN_ID,   send_Saved_Charge_Locat_HS3,   {'ChrgLocId_D_Sav':0, 'ChrgLocSaved_B_Dsply':0x1}),
    (0.5, SEND_MSG, ChargeSettings_HS3_CAN_ID,       send_ChargeSettings_HS3,       {'ChrgProgIdSaved_D_Stat':0}),
    # Clear Unsaved location
    (0.5, SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':0}),
    
     # Add 5 UNSAVED location
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':1, 'latitude':41.883627, 'longitude':-87.634747}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':1}),
    
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':2, 'latitude':41.881550, 'longitude':-87.636116}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':2}),
    
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':3, 'latitude':41.880926, 'longitude':-87.636030}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':3}),
    
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':4, 'latitude':41.879020, 'longitude':-87.634493}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':4}),
    
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':5, 'latitude':41.877475, 'longitude':-87.634156}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':5}),
    
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':6, 'latitude':41.884916, 'longitude':-87.623124}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':6}),
    
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':7, 'latitude':41.886393, 'longitude':-87.620037}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':7}),
    
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':8, 'latitude':41.893823, 'longitude':-87.61955}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':8}),
    
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':9, 'latitude':41.893795, 'longitude':-87.620766}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':9}),
    
    (2,   SEND_MSG, Unsaved_Charge_Locat_HS3_CAN_ID, send_Unsaved_Charge_Locat_HS3, {'ChrgLocId_D_Uns':10, 'latitude':41.883001, 'longitude':-87.634253}),
    (0.2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'ChrgLocIdCurnt_D_Uns':10}),

    (2, SEND_MSG, GWM_Send_Signals_10_HS3_CAN_ID, send_GWM_Send_Signals_10_HS3,   {'OfbChrgPrflUpdate_B_Rq':0}),
    (4, SEND_MSG,  GWM_HPCM_i_FrP14_CAN_ID, send_GWM_HPCM_i_FrP14, {'OfbChrgSetSync_D_Stat':0x2}),
]

if __name__ == '__main__':
    execute_test(TC_SET)
