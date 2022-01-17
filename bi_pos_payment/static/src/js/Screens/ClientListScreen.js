odoo.define('bi_pos_payment.ClientListScreen', function(require) {
	'use strict';

	const ClientListScreen = require('point_of_sale.ClientListScreen');
	const Registries = require('point_of_sale.Registries');
	const session = require('web.session');
	const core = require('web.core');
	const rpc = require('web.rpc');

	const _t = core._t;

	const BiClientListScreen = ClientListScreen => class extends ClientListScreen {
		register_payment() {
			var self = this;
			const partner_id = self.state.selectedClient;
			if (!partner_id) {

				self.showPopup('ErrorPopup', {
					'title': _t('Unknown customer'),
					'body': _t('You cannot Register Payment. Select customer first.'),
				});
				return false;
			}

			self.showPopup('RegisterPaymentPopupWidget', {'partner':self.state.selectedClient});
		}
	};

	Registries.Component.extend(ClientListScreen, BiClientListScreen);

	return ClientListScreen;

});