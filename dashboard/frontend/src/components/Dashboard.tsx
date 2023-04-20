// import React from 'react';
import React, { useEffect, useState } from "react";
import { MDBDataTable } from 'mdbreact';
import axios from 'axios';
import {Tap} from "./Tap";

const Dashboard = () => {
  const [data, setData] = useState<Tap[]>([]);

  useEffect(() => {
    axios
      .get<{ [key: string]: Tap }>("http://127.0.0.1:5000/", {
        headers: {
          "Content-Type": "application/json",
        },
      })
      .then((response) => {
        setData(Object.values(response.data));
        // console.log(Object.values(response.data));
      });
  }, []);

  const map_data = {
    columns: [
      {
        id: 'index',
        label: 'Index',
        field: 'index',        
        sort: 'asc',
        width: 100
      },
      {
        label: 'Organization',
        field: 'organization',
        sort: 'asc',
        width: 150
      },
      {
        label: 'Address',
        field: 'address',
        sort: 'asc',
        width: 150
      },
      {
        label: 'City',
        field: 'city',
        sort: 'asc',
        width: 150
      },
      {
        label: 'Phone',
        field: 'phone',
        sort: 'asc',
        width: 150
      },
    ],
    rows: data.map((item, index) => {
      return {
        ...item,
        index: index + 1,
        organization: item.organization,
        address: item.address,
        city: item.city,
        phone: item.phone
      }
    })
  };

  const customStyles = {
    headRow: {
      backgroundColor: '#0D47A1',
      color: '#fff',
      fontWeight: 'bold'
    },
    headCells: {
      textAlign: 'center'
    },
    rows: {
      backgroundColor: '#f5f5f5'
    },
    cells: {
      textAlign: 'center'
    }
  };
  

  return (
    <MDBDataTable
      striped
      bordered
      small
      hover
      data={map_data}
      customStyle={customStyles}
    />
  );
}

export default Dashboard;



// import React, { useEffect, useState } from "react";
// import axios from "axios";
// import Table from "./Table"; // import the Table component
// import {Tap} from "./Tap";
// import {TapFormProps} from "./TapForm";
// import TapForm from "./TapForm";
// import './Dashboard.css';

// const Dashboard = () => {
//   const [tapData, setTapData] = useState<Tap[]>([]); 
//   const [editingTap, setEditingTap] = useState<Tap | null>(null);

//   useEffect(() => {
//     axios
//       .get<{ [key: string]: Tap }>("http://127.0.0.1:5000/", {
//         headers: {
//           "Content-Type": "application/json",
//         },
//       })
//       .then((response) => {
//         setTapData(Object.values(response.data));
//         // console.log(Object.values(response.data));
//       });
//   }, []);
  

//   const handleFormSubmit = async (tap: Tap) => {
//     if (editingTap) {
//       try {
//         const response = await axios.put<Tap>(`http://127.0.0.1:5000/updatetap/${editingTap.tapnum}`, tap, {
//           headers: {
//             "Content-Type": "application/json",
//           },
//         });
//         const updatedTap = response.data;
//         setTapData((prevState) => {
//           const index = prevState.findIndex((t) => t.tapnum === updatedTap.tapnum);
//           if (index === -1) {
//             return prevState;
//           }
//           const newState = [...prevState];
//           newState.splice(index, 1, updatedTap);
//           return newState;
//         });
//         setEditingTap(null);
//       } catch (error) {
//         console.error("Error updating tap data:", error);
//       }
//     } else {
//       // Handle add logic here
//       console.log("Adding tap:", tap);
//     }
//   };
  

//   const handleEditTap = async (tap: Tap) => {
//     try {
//       const response = await axios.get<Tap>(`http://127.0.0.1:5000/updatetap/${tap.tapnum}`);
//       setEditingTap(response.data);
//       // check tap hours to see if it's an empty string
//       if (response.data.hours) {
//         console.log(response.data.hours);
//       }
//     } catch (error) {
//       console.error("Error fetching tap data:", error);
//     }
//   };

//   const handleDeleteTap = (tap: Tap) => {
//     // delete the tap from the API
//     console.log("Delete tap", tap);
//   };

//   const columns = React.useMemo(
//     () => [
//       {
//         Header: "TAP ID",
//         accessor: "tapnum",
//         pagination: true,
//       },
//       {
//         Header: "Organization",
//         accessor: "organization",
//         pagination: true,
//       },
//       {
//         Header: "Address",
//         accessor: "address",
//         pagination: true,
//       },
//       {
//         Header: "City",
//         accessor: "city",
//         pagination: true,
//       },
//       {
//         Header: "Phone",
//         accessor: "phone",
//         pagination: true,
//       },

//       {
//         Header: "Hours",
//         accessor: "hours",
//         pagination: true,
//       }
//       ,
        
//       {
//         Header: "Actions",
//         id: "actions",
//         Cell: ({ row }: any) => (
//           <div>
//             <button id="editButton" onClick={() => handleEditTap(row.original)}>Edit</button>
//             <button id="deleteButton" onClick={() => handleDeleteTap(row.original)}>Delete</button>
//           </div>
//         ),
//       },
//     ],
//     []
//   );

//   return (
//     <div className="Dashboard">
//       {editingTap && <TapForm onSubmit={handleFormSubmit} editingTap={editingTap} />}
//       <Table columns={columns} data={tapData} />
//     </div>
//   );
// };

// export default Dashboard;