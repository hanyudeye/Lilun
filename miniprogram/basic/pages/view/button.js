Page({
    data: {
        "array": [
            {
                name: "1",
                value: "选择1"
            },
            {
                name: "2",
                value: "选择2"
            },

        ]
    }, submit() {
        wx.navigateTo({
            url: 'index',
            success: (result) => {

            },
            fail: () => { },
            complete: () => { }
        });
    }
})