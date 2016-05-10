FaceBs.RbrowUpTip = clamp(0,1, R_BrowTip_ctrl.translateY);
FaceBs.LbrowUpTip  = clamp(0,1, L_BrowTip_ctrl.translateY);
FaceBs.RbrowDownTip  = clamp( 0,1,-R_BrowTip_ctrl.translateY);
FaceBs.LbrowDownTip  = clamp( 0,1,-L_BrowTip_ctrl.translateY);

FaceBs.RbrowUpMid  = clamp( 0,1,R_BrowMid_ctrl.translateY);
FaceBs.LbrowUpMid  = clamp( 0,1,L_BrowMid_ctrl.translateY);
FaceBs.RbrowDownMid  = clamp(0,1,-R_BrowMid_ctrl.translateY );
FaceBs.LbrowDownMid  = clamp( 0,1,-L_BrowMid_ctrl.translateY);

FaceBs.RbrowUpEnd  = clamp(0,1, R_BrowEnd_ctrl.translateY);
FaceBs.LbrowUpEnd  = clamp(0,1, L_BrowEnd_ctrl.translateY);
FaceBs.RbrowDownEnd  = clamp(0,1, -R_BrowEnd_ctrl.translateY);
FaceBs.LbrowDownEnd  = clamp(0,1, -L_BrowEnd_ctrl.translateY);

FaceBs.RbrowTipln  = clamp(0,1, -R_BrowTip_ctrl.translateX);
FaceBs.LbrowTipln  = clamp( 0,1,-L_BrowTip_ctrl.translateX);

FaceBs.REyeLidUpUp  = clamp(0,1, R_TLid_ctrl.translateY);    //////
FaceBs.LEyeLidUpUp  = clamp(0,1, L_TLid_ctrl.translateY);   ////////
FaceBs.REyeLidUpUpTip  = clamp(0,1, R_TLidTip_ctrl.translateY);
FaceBs.LEyeLidUpUpTip  = clamp(0,1, L_TLidTip_ctrl.translateY);





FaceBs.LEyeLidUpDown  = clamp(0,1, -L_TLid_ctrl.translateY);
FaceBs.REyeLidUpDown  = clamp(0,1, -R_TLid_ctrl.translateY);

FaceBs.REyeLidDownDown  = clamp(0,1, -R_BLid_ctrl.translateY);
FaceBs.LEyeLidDownDown  = clamp(0,1, -L_BLid_ctrl.translateY);

FaceBs.REyeLidDownUp  = clamp(0,1, R_BLid_ctrl.translateY);
FaceBs.LEyeLidDownUp  = clamp(0,1, L_BLid_ctrl.translateY);

FaceBs.REyeLidDownTip  = clamp(0,1, -R_TLidTip_ctrl.translateY);
FaceBs.LEyeLidDownTip  = clamp(0,1, -L_TLidTip_ctrl.translateY);

FaceBs.REyeLidDownUpTip  = clamp(0,1, R_BLidTip_ctrl.translateY);
FaceBs.LEyeLidDownUpTip  = clamp(0,1, L_BLidTip_ctrl.translateY);

FaceBs.REyeLidDownUpMid  = clamp(0,1, R_BLidEnd_ctrl.translateY);
FaceBs.LEyeLidDownUpMid  = clamp(0,1, L_BLidEnd_ctrl.translateY);

FaceBs.Rsquint  = clamp(0,1,R_Squint_ctrl.translateY );
FaceBs.Lsquint  = clamp( 0,1,L_Squint_ctrl.translateY );

FaceBs.RNoseSneer  = clamp(0,1,R_NoseSneer_ctrl.translateX);
FaceBs.LNoseSneer  = clamp( 0,1,L_NoseSneer_ctrl.translateX);
FaceBs.RCheekOut  = clamp(0,1, R_Cheek_ctrl.translateX);
FaceBs.LCheekOut  = clamp(0,1, L_Cheek_ctrl.translateX);
FaceBs.RCheekIn  = clamp( 0,1,-R_Cheek_ctrl.translateX);
FaceBs.LCheekIn  = clamp(0,1, -L_Cheek_ctrl.translateX);

FaceBs.RlipSneer  = clamp( 0,1,-R_LipSneer_ctrl.translateY);
FaceBs.LlipSneer  = clamp(0,1, -L_LipSneer_ctrl.translateY);

FaceBs.RlipCornerUp  = clamp(0,1, R_LipCorner_ctrl.translateY); 
FaceBs.LlipCornerUp  = clamp( 0,1, L_LipCorner_ctrl.translateY);
FaceBs.RlipCornerDown  = clamp(0,1,-R_LipCorner_ctrl.translateY );
FaceBs.LlipCornerDown  = clamp(0,1, -L_LipCorner_ctrl.translateY);

FaceBs.RlipCornerOut  = clamp(0,1, R_LipCorner_ctrl.translateX);
FaceBs.LlipCornerOut  = clamp( 0,1,L_LipCorner_ctrl.translateX);
FaceBs.RlipConrnerIn  = clamp(0,1, -R_LipCorner_ctrl.translateX);
FaceBs.LlipConrnerIn  = clamp(0,1, -L_LipCorner_ctrl.translateX);
FaceBs.MouthDown  = clamp(0,1, -M_mouth_ctrl.translateY);
FaceBs.MouthUp  = clamp(0,1, M_mouth_ctrl.translateY);

FaceBs.H  = clamp( 0,1,H_ctrl.translateX);
FaceBs.F  = clamp(0,1, F_ctrl.translateX);
FaceBs.A  = clamp(0,1, A_ctrl.translateX);
FaceBs.E  = clamp( 0,1,E_ctrl.translateX);
FaceBs.O  = clamp(0,1, O_ctrl.translateX);
FaceBs.U  = clamp(0,1, U_ctrl.translateX);
FaceBs.M  = clamp( 0,1,M_ctrl.translateX);

FKExtraJaw_M.rotateY = -M_mouth_ctrl.translateX *15;
FKExtraJaw_M.rotateZ = -M_mouth_ctrl.translateY *15;