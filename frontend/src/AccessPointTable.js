import React, { Component } from 'react';

class AccessPointTable extends Component {

  render() {
    return (
      <table className="table table-hover">
        <thead>
          <tr>
            <th>ESSID</th>
            <th>BSSID</th>
            <th># Clients</th>
          </tr>
        </thead>
        <tbody>
          {
            this.props.accessPoints.map((ap) => {
              return (
                <tr key={ap.bssid} onClick={() => { this.props.selectFunc(ap)}}>
                  <td>{ap.essid}</td>
                  <td>{ap.bssid}</td>
                  <td>{ap.clients.length}</td>
                </tr>
              )
            })
          }
        </tbody>
      </table>
    );
  }
}

export default AccessPointTable;
