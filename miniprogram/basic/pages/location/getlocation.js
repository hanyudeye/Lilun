Page({
    getlocation() {
        wx.getLocation({
            type: 'wgs84',
            altitude: false,
            success: (result) => {
                console.log(result)
            },
        });
    }, chooselocation() {
        wx.chooseLocation({
            success: (result) => {
                console.log(result)

                wx.openLocation({
                    latitude: result.latitude,
                    longitude: result.longitude,
                    scale: 28,
                    name: '',
                    address: '',
                    success: (result) => {
                        console.log(result)
                    },
                });

            },
        });
    }, openlocation() {
    }
})