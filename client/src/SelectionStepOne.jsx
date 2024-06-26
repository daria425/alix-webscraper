import PropTypes from "prop-types";
export default function SelectionStepOne({ getMainCategories }) {
  const regions = ["camden", "islington"];
  return (
    <>
      <p className="search__heading">Select a council to begin:</p>
      {regions.map((region) => (
        <button key={region} onClick={() => getMainCategories(region)}>
          {region[0].toUpperCase() + region.slice(1)}
        </button>
      ))}
    </>
  );
}

SelectionStepOne.propTypes = {
  getMainCategories: PropTypes.func,
};
