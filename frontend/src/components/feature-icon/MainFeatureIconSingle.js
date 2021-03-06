import PropTypes from "prop-types";
import React from "react";
import { REACT_BACKEND_URL } from "utils/url";

const MainFeatureIconSingle = ({ data, spaceBottomClass }) => {
  return (
    <div className="col-lg-4 col-md-6 col-sm-6">
      <div
        className={`support-wrap-3 text-center ${
          spaceBottomClass ? spaceBottomClass : ""
        }`}
        style={{ backgroundColor: `${data.backgroundColor}` }}
      >
        <div className="support-icon-2">
          <img
            className="animated"
            src={REACT_BACKEND_URL + data.iconImage}
            alt=""
          />
        </div>
        <div className="support-content-3">
          <img src={REACT_BACKEND_URL + data.titleImage} alt="" />
          <p>{data.title}</p>
        </div>
      </div>
    </div>
  );
};

MainFeatureIconSingle.propTypes = {
  data: PropTypes.object,
  spaceBottomClass: PropTypes.string
};

export default MainFeatureIconSingle;
