
KindEditor.ready(function(K) {
    window.editor = K.create('textarea[id = "id_content"]', {
        width : "800px",
        height : "500px",
        uploadJson: '/admin/uploads/kindeditor',
    });
});