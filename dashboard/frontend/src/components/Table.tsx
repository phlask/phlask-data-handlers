import { useMemo, useState, useCallback } from "react";
import { useTable, useSortBy, usePagination, useFilters} from "react-table";
import TimeConfig  from "./TimeConfig";
import Dropdown from "./Dropdown";

interface TableProps {
  columns: any[];
  data: any[];
}

const { getHourOptions } = TimeConfig;

const Table = ({ columns, data }: TableProps) => {
  const handleHourChange = useCallback((value: any) => {
    const { open, close } = JSON.parse(value);
    console.log(open, close);
  }, []);
  
  const filterTypes = useMemo(
    () => ({
      text: (rows: any[], id: any, filterValue: any) => {
        return rows.filter((row) => {
          const rowValue = row.values[id];
          return rowValue !== undefined
            ? String(rowValue).toLowerCase().startsWith(String(filterValue).toLowerCase())
            : true;
        });
      },
    }),
    []
  );

  interface InputFilterProps {
    column: {
      filterValue: any;
      setFilter: (value: any) => void;
      Header: string;
      canFilter?: boolean;
    };
  }

  const InputFilter = ({ column }: InputFilterProps) => {
    const { filterValue, setFilter } = column;
    
    return (
      <input value={filterValue || ""} onChange={(e) => setFilter(e.target.value || undefined)} placeholder={`Search ${column.Header}`} />
    );
  };
const defaultColumn = useMemo(
    () => ({
      Filter: InputFilter,
    }),
    [InputFilter]
  );

  const [pageSize, setPageSize] = useState(10);

  const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    prepareRow,
    page,
    gotoPage,
    pageCount,
    nextPage,
    previousPage,
    canNextPage,
    canPreviousPage,
    pageOptions,
    state: { pageIndex },
  } = useTable(
    {
      columns,
      data,
      defaultColumn,
      filterTypes,
      initialState: { pageIndex: 0, pageSize },
    },
    useFilters,
    useSortBy,
    usePagination
  );
  

  const pageSizeOptions = [10, 25, 50, 100];

  return (
    <>
    <pre>
      <code>
        {/* {JSON.stringify(
          {
            pageIndex,
            pageSize,
            pageCount: pageOptions.length,
            canNextPage,
            canPreviousPage,
          },
          null,
          2
        )} */}
      </code>
    </pre>
      <table {...getTableProps()}>
        <thead>
          {headerGroups.map((headerGroup) => (
            <tr {...headerGroup.getHeaderGroupProps()}>
              {headerGroup.headers.map((column) => (
                <th {...column.getHeaderProps(column.getSortByToggleProps())}>
                  {column.render("Header")}
                  <span>{column.isSorted ? (column.isSortedDesc ? " 🔽" : " 🔼") : ""}</span>
                  <div>{column.canFilter ? column.render("Filter") : null}</div>
                </th>
              ))}
            </tr>
          ))}
        </thead>
        <tbody {...getTableBodyProps()}>
        {page.map((row: any, i: number) => {
          prepareRow(row);
          return (
            <tr {...row.getRowProps()} key={i}>
              {row.cells.map((cell: any, j: number) => {
                return (
                  <td {...cell.getCellProps()} key={j}>
                    {typeof cell.value === "object" && cell.value !== null ? (
                      <Dropdown options={getHourOptions(cell.value)} onChange={handleHourChange} value={cell.value} />
                    ) : (
                      cell.render("Cell")
                    )}
                  </td>
                );
              })}
            </tr>
            );
          })}
        </tbody>
      </table>
      <div className="pagination" id="pag-buttons">
        <button onClick={() => gotoPage(0)} disabled={!canPreviousPage}>
          {'<<'}
        </button>{' '}
        <button onClick={() => previousPage()} disabled={!canPreviousPage}>
          {'<'}
        </button>{' '}
        <button onClick={() => nextPage()} disabled={!canNextPage}>
          {'>'}
        </button>{' '}
        <button onClick={() => gotoPage(pageCount - 1)} disabled={!canNextPage}>
          {'>>'}
        </button>{' '}
        <span>
          Page{' '}
          <strong>
            {pageIndex + 1} of {pageOptions.length}
          </strong>{' '}
        </span>
        <select
          value={pageSize}
          onChange={e => {
            setPageSize(Number(e.target.value))
          }}
        >
          {pageSizeOptions.map(pageSize => (
            <option key={pageSize} value={pageSize}>
              Show {pageSize}
            </option>
          ))}
        </select>
      </div>
    </>
  );
};


export default Table;
