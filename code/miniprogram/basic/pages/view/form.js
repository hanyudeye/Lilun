Page({
    data: {
        array: ["选择1", "选择2", "选择3"],
        index: 1
    },
    change(e) {
        this.setData({
            index: e.detail.value
        })
        console.log(e.detail.value)
    }, switchChange(e) {
        console.log(e.detail.value)
    }

})