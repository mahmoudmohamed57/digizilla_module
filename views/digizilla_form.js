odoo.define('digizilla_module.digizilla_form', function (require) {
    "use strict";

    var FormView = require('web.FormView');

    FormView.include({
        render_buttons: function () {
            this._super.apply(this, arguments);
            if (this.$buttons) {
                this.$buttons.find('.o_form_button_create').hide();
            }
        },
    });
});
