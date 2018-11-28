import React, { Component } from 'react';
import Navbar from './Navbar'
import AccessPointTable from './AccessPointTable'
import ClientTable from './ClientTable';
import * as API from './api'

class App extends Component {
  constructor() {
    super();
    this.state = { 
      selectedAP: null,
      refreshing: false,
      aps: null
    };
  }

  onSelect = (ap) => {
    this.setState({selectedAP : ap});
  }

  refresh = () => {
    this.setState({refreshing: true})
    API.search().then((aps) => {
      this.setState({aps: aps})
    }).always(() => {
      this.setState({refreshing: false})
    })
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
            <div className="col-12">
              <button className="btn btn-primary mb-3" disabled={this.state.refreshing} onClick={() => this.refresh()}>{this.state.refreshing ? 'Refreshing' : 'Refresh'}</button>
            </div>
            <div className="col-12 col-md-8 col-lg-8">
              <AccessPointTable accessPoints={this.state.aps} selectFunc={this.onSelect}/>
            </div>
            <div className="col-12 col-md-4 col-lg-4">
              <ClientTable ap={this.state.selectedAP}/>
            </div>
          </div>
        </div>
      </>
    );
  }
}

export default App;
