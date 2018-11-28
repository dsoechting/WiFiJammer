import React, { Component } from 'react';
import Navbar from './Navbar'
import AccessPointTable from './AccessPointTable'
import {AccessPoints} from './data'
import ClientTable from './ClientTable';

class App extends Component {
  constructor() {
    super();
    this.state = { selectedAP: null };
  }

  onSelect = (ap) => {
    this.setState({selectedAP : ap});
  }

  render() {
    return (
      <>
        <Navbar/>
        <div className="container-fluid">
          <div className="row">
            <div className="col-12">
              <p className="h5 my-3 text-center">Welcome to WifiJammer. Click the refresh icon to load a list of access points. Select an access point, and then select a client to jam from the network.</p>
            </div>
            <div className="col-6">
              <AccessPointTable accessPoints={AccessPoints} selectFunc={this.onSelect}/>
            </div>
            <div className="col-6">
              <ClientTable ap={this.state.selectedAP}/>
            </div>
          </div>
        </div>
      </>
    );
  }
}

export default App;
