import PropTypes from "prop-types";
import React from "react";
import { Link } from "react-router-dom";
import Tab from "react-bootstrap/Tab";
import Nav from "react-bootstrap/Nav";
import SectionTitleThree from "../../components/section-title/SectionTitleThree";
import ProductMainGrid from "./ProductMainGrid";
import { productListSelector } from "recoil/productRecoil";
import { useRecoilState } from "recoil";

const TabProductList = ({
  spaceTopClass,
  spaceBottomClass,
  category,
  containerClass,
  extraClass
}) => {

  const [products, setProducts] = useRecoilState(productListSelector);

  return (
    <div
      className={`product-area ${spaceTopClass ? spaceTopClass : ""} ${
        spaceBottomClass ? spaceBottomClass : ""
      } ${extraClass ? extraClass : ""}`}
    >
      <div className={`${containerClass ? containerClass : "container"}`}>
        <SectionTitleThree
          titleText="Featured Products"
          positionClass="text-center"
        />
        <Tab.Container defaultActiveKey="all">
          
          <Nav
            variant="pills"
            className="product-tab-list pt-30 pb-55 text-center"
          >
            <Nav.Item>
              <Nav.Link eventKey="all">
              </Nav.Link>
            </Nav.Item>
            {/*
            <Nav.Item>
              <Nav.Link eventKey="men">
                <h4>Men</h4>
              </Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link eventKey="women">
                <h4>Women</h4>
              </Nav.Link>
            </Nav.Item>
            */}
          </Nav>
          <Tab.Content>
            <Tab.Pane eventKey="all">
              <div className="row">
                <ProductMainGrid
                  category="all"
                  limit={4}
                  spaceBottomClass="mb-25"
                  products = {products} 
                />
              </div>
            </Tab.Pane>
            {/*
            <Tab.Pane eventKey="men">
              <div className="row">
                <ProductMainGrid
                  category="men"
                  limit={4}
                  spaceBottomClass="mb-25"
                />
              </div>
            </Tab.Pane>
            <Tab.Pane eventKey="women">
              <div className="row">
                <ProductMainGrid
                  category={category}
                  type="women"
                  limit={4}
                  spaceBottomClass="mb-25"
                />
              </div>
            </Tab.Pane>
            */}
          </Tab.Content>
        </Tab.Container>
        <div className="view-more round-btn text-center mt-20 toggle-btn6 col-12">
          <Link
            className="loadMore6"
            to={process.env.PUBLIC_URL + "/shop-grid-standard"}
          >
            Discover More
          </Link>
        </div>
      </div>
    </div>
  );
};

TabProductList.propTypes = {
  category: PropTypes.string,
  containerClass: PropTypes.string,
  extraClass: PropTypes.string,
  spaceBottomClass: PropTypes.string,
  spaceTopClass: PropTypes.string
};

export default TabProductList;
