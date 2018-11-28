import React, { Component } from 'react';
import * as API from './api'

class AccessPointTable extends Component {
  jamNetwork(ap) {
    API.attackAll(ap.bssid, ap.channel);
  }

  render() {
    return (
      <table className="table table-hover">
        <thead>
          <tr>
            <th>ESSID</th>
            <th>BSSID</th>
            <th>Channel</th>
            <th># Clients</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {
            this.props.accessPoints === null ?
            <tr className="text-center"><td colSpan="5">Refresh the list to see available access points.</td></tr>
            :
            (this.props.accessPoints.length === 0 ?
              <tr className="text-center"><td colSpan="5">No access points were found.</td></tr>              
              :
              this.props.accessPoints.map((ap) => {
              return (
                <tr key={ap.bssid} onClick={() => { this.props.selectFunc(ap)}}>
                  <td>{ap.essid}</td>
                  <td>{ap.bssid}</td>
                  <td>{ap.channel}</td>
                  <td>{ap.clients.length}</td>
                  <td>
                    <button className="btn btn-sm btn-primary" onClick={() => this.jamNetwork(ap)}>Jam Network</button>
                  </td>
                </tr>
              )
            }))
          }
        </tbody>
      </table>
    );
  }
}

export default AccessPointTable;
