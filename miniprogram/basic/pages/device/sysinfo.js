Page({

    getsysteminfo() {
        wx.getSystemInfo({
            success: (result) => {
                console.log(result)
            },
        });
    },getnetworktype(){
        wx.getNetworkType({
            success: (result)=>{
                console.log(result)
            },
        });
    },makephone(){
        wx.makePhoneCall({
            phoneNumber: "181123123",
            success: (result)=>{
               console.log(result) 
            },
        });
    },scan(){
        wx.scanCode({
            onlyFromCamera: false,
            scanType: ['qrCode','barCode','datamatrix','pdf417'],
            success: (result)=>{
               console.log(result) 
            },
        });
    }
})