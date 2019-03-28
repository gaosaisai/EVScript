Saved_Charge_Locat_HS3_CAN_ID = '3F4'
def send_Saved_Charge_Locat_HS3(args):
    # Defined values for latitude and longitude out of range:
    # 'latitude'  : -90.048575
    # 'longitude' : -256.048575
    
    acceptable_args = ['ChrgLocId_D_Sav', 'ChrgNowCurnt_B_Dsply', 'latitude', 'longitude', 'ChrgLocSaved_B_Dsply']
    received_args = args.keys()
    wrong_args = [i for i in received_args if i not in acceptable_args]
    if len(wrong_args) > 0:
        print 'Received unaccepted argument: {}'.format(wrong_args)
        exit()
    
    signals = args
    
    signals_string = ''
    message_name = 'Saved_Charge_Locat_HS3'
    
    if 'ChrgLocId_D_Sav' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgLocId_D_Sav', signals['ChrgLocId_D_Sav'])
    
    if 'ChrgNowCurnt_B_Dsply' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgNowCurnt_B_Dsply', signals['ChrgNowCurnt_B_Dsply'])
    
    
    if 'latitude' in args:
        latt_whole = int(signals['latitude'])
        latt_frct  = int('{:<06}'.format(str(float(signals['latitude'])).split('.')[-1]))
        
        if latt_whole == -90:
            latt_whole = -89
            latt_frct  = 1000000 + latt_frct
        
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgLocLattDeg_An_Sav', abs(latt_whole))
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgLocLattPostv_B_Sav', int(latt_whole >= 0))
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgLocLattFrct_An_Sav', latt_frct)
    
    
    if 'longitude' in args:
        long_whole = int(signals['longitude'])
        long_frct  = int('{:<06}'.format(str(float(signals['longitude'])).split('.')[-1]))
        
        if long_whole == -256:
            long_whole = -255
            long_frct  = 1000000 + long_frct
        
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgLocLongDeg_An_Sav', abs(long_whole))
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgLocLongPostv_B_Sav', int(long_whole >= 0))
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgLocLongFrct_An_Sav', long_frct)
    
    if 'ChrgLocSaved_B_Dsply' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgLocSaved_B_Dsply', signals['ChrgLocSaved_B_Dsply'])
    
    # remove first character ','
    signals_string = signals_string[1:]
    
    print '\nSENDING Saved_Charge_Locat_HS3:\t {}'.format(signals_string)
    
    return signals_string


ChargeSettings_HS3_CAN_ID = '3F5'
def send_ChargeSettings_HS3(args):
    signals = args
    
    acceptable_args = ['ChrgToPcWkndSav_D_Stat', 'ChrgToPcWkdySav_D_Stat', 'ChrgProgIdSaved_D_Stat', 'ChrgNowEnbl_B_Saved', 'ChrgLocIdUnsAck_B_Stat', 'ChrgLocIdCurnt_D_Sav', 'ChrgPrflWkdy_No_Actl', 'ChrgPrflWknd_No_Actl']
    received_args = args.keys()
    wrong_args = [i for i in received_args if i not in acceptable_args]
    if len(wrong_args) > 0:
        print 'Received unaccepted argument: {}'.format(wrong_args)
        exit()
    
    signals_string = ''
    message_name = 'ChargeSettings_HS3'
    
    if 'ChrgToPcWkndSav_D_Stat' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgToPcWkndSav_D_Stat', signals['ChrgToPcWkndSav_D_Stat'])
    if 'ChrgToPcWkdySav_D_Stat' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgToPcWkdySav_D_Stat', signals['ChrgToPcWkdySav_D_Stat'])
    if 'ChrgProgIdSaved_D_Stat' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgProgIdSaved_D_Stat', signals['ChrgProgIdSaved_D_Stat'])
    if 'ChrgNowEnbl_B_Saved' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgNowEnbl_B_Saved',    signals['ChrgNowEnbl_B_Saved'])
    if 'ChrgLocIdUnsAck_B_Stat' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgLocIdUnsAck_B_Stat', signals['ChrgLocIdUnsAck_B_Stat'])
    if 'ChrgLocIdCurnt_D_Sav' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgLocIdCurnt_D_Sav',   signals['ChrgLocIdCurnt_D_Sav'])
    if 'ChrgPrflWkdy_No_Actl' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgPrflWkdy_No_Actl',   signals['ChrgPrflWkdy_No_Actl'])
    if 'ChrgPrflWknd_No_Actl' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgPrflWknd_No_Actl',   signals['ChrgPrflWknd_No_Actl'])
    
    # remove first character ','
    signals_string = signals_string[1:]
    
    print '\nSENDING ChargeSettings_HS3:\t {}'.format(signals_string)
    
    return signals_string


APIM_Request_Signals_5_CAN_ID = '211'
def recv_APIM_Request_Signals_5(args):
    signals = args
    
    acceptable_args = ['OnbChrgPrflUpdate_B_Rq', 'OnbChrgLocIdUns_B_Rq', 'OnbChrgLocIdTrgt_No_Rq', 'OnbChrgSetDelete_B_Rq', 'OnbChrgSetNow_D_Rq', 'OnbChrgToPcWkdy_D_Actl', 'OnbChrgToPcWknd_D_Actl', 'OnbChrgPrflWkdy_No_Rq', 'OnbChrgPrflWknd_No_Rq']
    received_args = args.keys()
    wrong_args = [i for i in received_args if i not in acceptable_args]
    if len(wrong_args) > 0:
        print 'Received unaccepted argument: {}'.format(wrong_args)
        exit()
    
    signals_string = ''
    message_name = 'APIM_Request_Signals_5'
    
    if 'OnbChrgPrflUpdate_B_Rq' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OnbChrgPrflUpdate_B_Rq', signals['OnbChrgPrflUpdate_B_Rq'])
    if 'OnbChrgLocIdUns_B_Rq' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OnbChrgLocIdUns_B_Rq',   signals['OnbChrgLocIdUns_B_Rq'])
    if 'OnbChrgLocIdTrgt_No_Rq' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OnbChrgLocIdTrgt_No_Rq', signals['OnbChrgLocIdTrgt_No_Rq'])
    if 'OnbChrgSetDelete_B_Rq' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OnbChrgSetDelete_B_Rq',  signals['OnbChrgSetDelete_B_Rq'])
    if 'OnbChrgSetNow_D_Rq' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OnbChrgSetNow_D_Rq',     signals['OnbChrgSetNow_D_Rq'])
    if 'OnbChrgToPcWkdy_D_Actl' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OnbChrgToPcWkdy_D_Actl', signals['OnbChrgToPcWkdy_D_Actl'])
    if 'OnbChrgToPcWknd_D_Actl' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OnbChrgToPcWknd_D_Actl', signals['OnbChrgToPcWknd_D_Actl'])
    if 'OnbChrgPrflWkdy_No_Rq' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OnbChrgPrflWkdy_No_Rq',  signals['OnbChrgPrflWkdy_No_Rq'])
    if 'OnbChrgPrflWknd_No_Rq' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OnbChrgPrflWknd_No_Rq',  signals['OnbChrgPrflWknd_No_Rq'])
    
    # remove first character ','
    signals_string = signals_string[1:]
    
    print '\nWAITING FOR APIM_Request_Signals_5:\t {}'.format(signals_string)
    
    return signals_string


Unsaved_Charge_Locat_HS3_CAN_ID = '3F3'
def send_Unsaved_Charge_Locat_HS3(args):
    # Defined values for latitude and longitude out of range:
    # 'latitude'  : -90.048575
    # 'longitude' : -256.048575
    
    acceptable_args = ['ChrgLocId_D_Uns', 'latitude', 'longitude']
    received_args = args.keys()
    wrong_args = [i for i in received_args if i not in acceptable_args]
    if len(wrong_args) > 0:
        print 'Received unaccepted argument: {}'.format(wrong_args)
        exit()
    
    signals = args
    
    signals_string = ''
    message_name = 'Unsaved_Charge_Locat_HS3'
    
    if 'ChrgLocId_D_Uns' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgLocId_D_Uns', signals['ChrgLocId_D_Uns'])
    
    
    if 'latitude' in args:
        latt_whole = int(signals['latitude'])
        latt_frct  = int('{:<06}'.format(str(float(signals['latitude'])).split('.')[-1]))
        
        if latt_whole == -90:
            latt_whole = -89
            latt_frct  = 1000000 + latt_frct
        
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgLocLattDeg_An_Uns',  abs(latt_whole))
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgLocLattPostv_B_Uns', int(latt_whole >= 0))
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgLocLattFrct_An_Uns', latt_frct)
    
    
    if 'longitude' in args:
        long_whole = int(signals['longitude'])
        long_frct  = int('{:<06}'.format(str(float(signals['longitude'])).split('.')[-1]))
        
        if long_whole == -256:
            long_whole = -255
            long_frct  = 1000000 + long_frct
        
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgLocLongDeg_An_Uns',  abs(long_whole))
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgLocLongPostv_B_Uns', int(long_whole >= 0))
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgLocLongFrct_An_Uns', long_frct)
    
    # remove first character ','
    signals_string = signals_string[1:]
    
    print '\nSENDING Unsaved_Charge_Locat_HS3:\t {}'.format(signals_string)
    
    return signals_string


GWM_Send_Signals_10_HS3_CAN_ID = '281'
def send_GWM_Send_Signals_10_HS3(args):
    signals = args
    
    acceptable_args = ['ChrgGoTElement_D_Stat', 'ChrgGoTHr_T_Stat', 'ChrgGoTMnte_D_Stat', 'ChrgGoTPrcond_D_Stat', 'ChrgGoTAllOn_B_Stat', 'ChrgGoTNext_D_Stat', 'OfbChrgPrflUpdate_B_Rq', 'ChrgLocIdCurnt_D_Uns', 'ChrgGoTElement_B_Dsply']
    received_args = args.keys()
    wrong_args = [i for i in received_args if i not in acceptable_args]
    if len(wrong_args) > 0:
        print 'Received unaccepted argument: {}'.format(wrong_args)
        exit()
    
    signals_string = ''
    message_name = 'GWM_Send_Signals_10_HS3'
    
    if 'ChrgGoTElement_D_Stat' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgGoTElement_D_Stat',    signals['ChrgGoTElement_D_Stat'])
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgGoTElement_D_Stat_UB', 0x01)
    else:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgGoTElement_D_Stat_UB', 0x00)
    
    if 'ChrgGoTHr_T_Stat' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgGoTHr_T_Stat',    signals['ChrgGoTHr_T_Stat'])
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgGoTHr_T_Stat_UB', 0x01)
    else:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgGoTHr_T_Stat_UB', 0x00)
    
    if 'ChrgGoTMnte_D_Stat' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgGoTMnte_D_Stat',    signals['ChrgGoTMnte_D_Stat'])
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgGoTMnte_D_Stat_UB', 0x01)
    else:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgGoTMnte_D_Stat_UB', 0x00)
    
    if 'ChrgGoTPrcond_D_Stat' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgGoTPrcond_D_Stat',    signals['ChrgGoTPrcond_D_Stat'])
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgGoTPrcond_D_Stat_UB', 0x01)
    else:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgGoTPrcond_D_Stat_UB', 0x00)
    
    if 'ChrgGoTAllOn_B_Stat' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgGoTAllOn_B_Stat',    signals['ChrgGoTAllOn_B_Stat'])
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgGoTAllOn_B_Stat_UB', 0x01)
    else:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgGoTAllOn_B_Stat_UB', 0x00)
    
    if 'ChrgGoTNext_D_Stat' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgGoTNext_D_Stat',    signals['ChrgGoTNext_D_Stat'])
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgGoTNext_D_Stat_UB', 0x01)
    else:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgGoTNext_D_Stat_UB', 0x00)
    
    if 'OfbChrgPrflUpdate_B_Rq' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OfbChrgPrflUpdate_B_Rq',    signals['OfbChrgPrflUpdate_B_Rq'])
        signals_string += ',{}_{}:{}'.format(message_name, 'OfbChrgPrflUpdate_B_Rq_UB', 0x01)
    else:
        signals_string += ',{}_{}:{}'.format(message_name, 'OfbChrgPrflUpdate_B_Rq_UB', 0x00)
    
    if 'ChrgLocIdCurnt_D_Uns' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgLocIdCurnt_D_Uns',    signals['ChrgLocIdCurnt_D_Uns'])
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgLocIdCurnt_D_Uns_UB', 0x01)
    else:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgLocIdCurnt_D_Uns_UB', 0x00)
    
    if 'ChrgGoTElement_B_Dsply' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgGoTElement_B_Dsply',    signals['ChrgGoTElement_B_Dsply'])
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgGoTElement_B_Dsply_UB', 0x01)
    else:
        signals_string += ',{}_{}:{}'.format(message_name, 'ChrgGoTElement_B_Dsply_UB', 0x00)
    
    # remove first character ','
    signals_string = signals_string[1:]
    
    print '\nSENDING GWM_Send_Signals_10_HS3:\t {}'.format(signals_string)
    return signals_string


APIM_Send_Signals_2_CAN_ID = '215'
def recv_APIM_Send_Signals_2(args):
    signals = args
    
    acceptable_args = ['OnbChrgGoTUpdate_B_Rq', 'OnbChrgGoTElement_D_Rq', 'OnbChrgGoTHr_T_Rq', 'OnbChrgGoTMnte_D_Rq', 'OnbChrgGoTPrcond_D_Rq', 'OnbChrgGoTOn_D_Rq', 'OnbChrgClearAll_B_Rq', 'OnbChrgGoTDelete_B_Rq', 'OnbChrgGoTExtHtr_D_Rq', 'OnbChrgGoTTouch_D_Rq']
    received_args = args.keys()
    wrong_args = [i for i in received_args if i not in acceptable_args]
    if len(wrong_args) > 0:
        print 'Received unaccepted argument: {}'.format(wrong_args)
        exit()
    
    message_name = 'APIM_Send_Signals_2'
    signals_string = ''
    
    if 'OnbChrgGoTUpdate_B_Rq' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OnbChrgGoTUpdate_B_Rq', signals['OnbChrgGoTUpdate_B_Rq'])
    if 'OnbChrgGoTElement_D_Rq' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OnbChrgGoTElement_D_Rq', signals['OnbChrgGoTElement_D_Rq'])
    if 'OnbChrgGoTHr_T_Rq' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OnbChrgGoTHr_T_Rq', signals['OnbChrgGoTHr_T_Rq'])
    if 'OnbChrgGoTMnte_D_Rq' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OnbChrgGoTMnte_D_Rq', signals['OnbChrgGoTMnte_D_Rq'])
    if 'OnbChrgGoTPrcond_D_Rq' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OnbChrgGoTPrcond_D_Rq', signals['OnbChrgGoTPrcond_D_Rq'])
    if 'OnbChrgGoTOn_D_Rq' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OnbChrgGoTOn_D_Rq', signals['OnbChrgGoTOn_D_Rq'])
    if 'OnbChrgClearAll_B_Rq' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OnbChrgClearAll_B_Rq', signals['OnbChrgClearAll_B_Rq'])
    if 'OnbChrgGoTDelete_B_Rq' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OnbChrgGoTDelete_B_Rq', signals['OnbChrgGoTDelete_B_Rq'])
    if 'OnbChrgGoTExtHtr_D_Rq' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OnbChrgGoTExtHtr_D_Rq', signals['OnbChrgGoTExtHtr_D_Rq'])
    if 'OnbChrgGoTTouch_D_Rq' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OnbChrgGoTTouch_D_Rq', signals['OnbChrgGoTTouch_D_Rq'])
    
    # remove first character ','
    signals_string = signals_string[1:]
    
    print '\nWAITING FOR APIM_Send_Signals_2:\t {}'.format(signals_string)
    
    return signals_string


GWM_Send_Signals_9_HS3_CAN_ID = '274'
def send_GWM_Send_Signals_9_HS3(args):
    signals = args
    
    acceptable_args = ['PwFlwBattClimt_B_Dsply', 'PwFlwBatt_D_Dsply', 'PwFlwFuelDrv_D_Dsply', 'PwFlwFuelClimt_B_Dsply', 'PwFlwFuelBatt_B_Dsply', 'PwFlwBattGen_D_Dsply', 'OfbChrgGoTUpdate_B_Rq']
    received_args = args.keys()
    wrong_args = [i for i in received_args if i not in acceptable_args]
    if len(wrong_args) > 0:
        print 'Received unaccepted argument: {}'.format(wrong_args)
        exit()
    
    message_name = 'GWM_Send_Signals_9_HS3'
    signals_string = ''
    
    if 'PwFlwBattClimt_B_Dsply' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'PwFlwBattClimt_B_Dsply', signals['PwFlwBattClimt_B_Dsply'])
        signals_string += ',{}_{}:{}'.format(message_name, 'PwFlwBattClimt_B_Dsply_UB', 0x01)
    else:
        signals_string += ',{}_{}:{}'.format(message_name, 'PwFlwBattClimt_B_Dsply_UB', 0x00)
    
    if 'PwFlwBatt_D_Dsply' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'PwFlwBatt_D_Dsply', signals['PwFlwBatt_D_Dsply'])
        signals_string += ',{}_{}:{}'.format(message_name, 'PwFlwBatt_D_Dsply_UB', 0x01)
    else:
        signals_string += ',{}_{}:{}'.format(message_name, 'PwFlwBatt_D_Dsply_UB', 0x00)
    
    if 'PwFlwFuelDrv_D_Dsply' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'PwFlwFuelDrv_D_Dsply', signals['PwFlwFuelDrv_D_Dsply'])
        signals_string += ',{}_{}:{}'.format(message_name, 'PwFlwFuelDrv_D_Dsply_UB', 0x01)
    else:
        signals_string += ',{}_{}:{}'.format(message_name, 'PwFlwFuelDrv_D_Dsply_UB', 0x00)
    
    if 'PwFlwFuelClimt_B_Dsply' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'PwFlwFuelClimt_B_Dsply', signals['PwFlwFuelClimt_B_Dsply'])
        signals_string += ',{}_{}:{}'.format(message_name, 'PwFlwFuelClimt_B_Dsply_UB', 0x01)
    else:
        signals_string += ',{}_{}:{}'.format(message_name, 'PwFlwFuelClimt_B_Dsply_UB', 0x00)
    
    if 'PwFlwFuelBatt_B_Dsply' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'PwFlwFuelBatt_B_Dsply', signals['PwFlwFuelBatt_B_Dsply'])
        signals_string += ',{}_{}:{}'.format(message_name, 'PwFlwFuelBatt_B_Dsply_UB', 0x01)
    else:
        signals_string += ',{}_{}:{}'.format(message_name, 'PwFlwFuelBatt_B_Dsply_UB', 0x00)
    
    if 'PwFlwBattGen_D_Dsply' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'PwFlwBattGen_D_Dsply', signals['PwFlwBattGen_D_Dsply'])
        signals_string += ',{}_{}:{}'.format(message_name, 'PwFlwBattGen_D_Dsply_UB', 0x01)
    else:
        signals_string += ',{}_{}:{}'.format(message_name, 'PwFlwBattGen_D_Dsply_UB', 0x00)
    
    if 'OfbChrgGoTUpdate_B_Rq' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OfbChrgGoTUpdate_B_Rq', signals['OfbChrgGoTUpdate_B_Rq'])
        signals_string += ',{}_{}:{}'.format(message_name, 'OfbChrgGoTUpdate_B_Rq_UB', 0x01)
    else:
        signals_string += ',{}_{}:{}'.format(message_name, 'OfbChrgGoTUpdate_B_Rq_UB', 0x00)
    
    # remove first character ','
    signals_string = signals_string[1:]
    
    print '\nSENDING GWM_Send_Signals_9_HS3:\t {}'.format(signals_string)
    
    return signals_string

TCU_Send_Signals_1_CAN_ID = '28B'
def send_TCU_Send_Signals_1(args):
    signals = args
    
    acceptable_args = ['OfbChrgSetSync_D_Rq']
    received_args = args.keys()
    wrong_args = [i for i in received_args if i not in acceptable_args]
    if len(wrong_args) > 0:
        print 'Received unaccepted argument: {}'.format(wrong_args)
        exit()
    
    message_name = 'TCU_Send_Signals_1'
    signals_string = ''
    
    if 'OfbChrgSetSync_D_Rq' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OfbChrgSetSync_D_Rq', signals['OfbChrgSetSync_D_Rq'])
    
    # remove first character ','
    signals_string = signals_string[1:]
    
    print '\nSENDING TCU_Send_Signals_1:\t {}'.format(signals_string)
    
    return signals_string

GWM_HPCM_i_FrP14_CAN_ID = '475'
def send_GWM_HPCM_i_FrP14(args):
    signals = args
    
    acceptable_args = ['OfbChrgSetSync_D_Stat']
    received_args = args.keys()
    wrong_args = [i for i in received_args if i not in acceptable_args]
    if len(wrong_args) > 0:
        print 'Received unaccepted argument: {}'.format(wrong_args)
        exit()
    
    message_name = 'GWM_HPCM_i_FrP14'
    signals_string = ''
    
    if 'OfbChrgSetSync_D_Stat' in args:
        signals_string += ',{}_{}:{}'.format(message_name, 'OfbChrgSetSync_D_Stat', signals['OfbChrgSetSync_D_Stat'])
    
    # remove first character ','
    signals_string = signals_string[1:]
    
    print '\nSENDING GWM_HPCM_i_FrP14:\t {}'.format(signals_string)
    
    return signals_string

