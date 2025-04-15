import { Component, useState } from "@odoo/owl";

export class Playground extends Component {
    static template = "mp_owl.playground";
    static props = {
        
    };
    setup() {
        this.state = useState({ value: 0 });
    }

    increment() {
        this.state.value++;
    }

    showMessage() {
        alert('Test 1234');
    }
}
