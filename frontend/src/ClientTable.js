import React, { Component } from 'react';

class ClientTable extends Component {
  jam(client) {
    console.log(client);
  }

  render() {
    return (
      <table className="table table-hover">
        <thead>
          <tr>
            <th>Client MAC</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {
            this.props.ap === null ? 
            <tr className="text-center"><td>No access point has been selected.</td></tr>
            :
            (this.props.ap.clients.length === 0 ? 
            <tr className="text-center"><td>Selected access point has no clients.</td></tr>
            :
            this.props.ap.clients.map((client) => {
              return (
                <tr>
                  <td>{client}</td>
                  <td>
                    <button className="btn btn-sm btn-outline-primary" onClick={() => this.jam(client)}>Jam</button>
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

export default ClientTable;
