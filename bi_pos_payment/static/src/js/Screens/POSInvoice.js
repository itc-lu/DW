odoo.define('point_of_sale.POSInvoice', function(require) {
	'use strict';

	const PosComponent = require('point_of_sale.PosComponent');
	const Registries = require('point_of_sale.Registries');

	class POSInvoice extends PosComponent {
		constructor() {
			super(...arguments);
		}

		get highlight() {
			return this.props.order !== this.props.selectedPosOrder ? '' : 'highlight';
		}
	}
	POSInvoice.template = 'POSInvoice';

	Registries.Component.add(POSInvoice);

	return POSInvoice;
});
