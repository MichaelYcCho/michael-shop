import PropTypes from "prop-types";
import React, { Fragment } from "react";
import MetaTags from "react-meta-tags";
import { BreadcrumbsItem } from "react-breadcrumbs-dynamic";
import LayoutOne from "../../layouts/LayoutOne";
import Breadcrumb from "../../wrappers/breadcrumb/Breadcrumb";
import RelatedProductSlider from "../../wrappers/product/RelatedProductSlider";
import ProductDescriptionTab from "../../wrappers/product/ProductDescriptionTab";
import ProductImageDescription from "../../wrappers/product/ProductImageDescription";

import { productListSelector } from "recoil/productRecoil";
import { useRecoilValue } from "recoil";

const ProductDetail = ({ location }) => {
  const { pathname } = location;

  const products = useRecoilValue(productListSelector);
  const productID = parseInt(pathname.split("/").reverse()[0])
 
  const getProduct = (products, productID ) => {
    if (products && productID) {
        return products.filter(
          product => product.pk === productID
        );
      }
  }
    const product = getProduct(products, productID)[0];

  return (
    <Fragment>
      <MetaTags>
        <title>Michael-Shop | Product Page</title>
        <meta
          name="description"
          content="Product page of Michael-Shop react minimalist eCommerce template."
        />
      </MetaTags>

      <BreadcrumbsItem to={process.env.PUBLIC_URL + "/"}>Home</BreadcrumbsItem>
      <BreadcrumbsItem to={process.env.PUBLIC_URL + pathname}>
        Shop Product
      </BreadcrumbsItem>

      <LayoutOne headerTop="visible">
        {/* breadcrumb */}
        <Breadcrumb />

        {/* product description with image */}
        <ProductImageDescription
          spaceTopClass="pt-100"
          spaceBottomClass="pb-100"
          product={product}
          galleryType="fixedImage"
        />

        {/* product description tab */}
        <ProductDescriptionTab
          spaceBottomClass="pb-90"
          product={product}
          productFullDesc={product.description}
        />

        {/* ToDo: Related Product Slider 같은 카테고리 기반 Product 출력예정
        <RelatedProductSlider
          spaceBottomClass="pb-95"
          category={product.category[0]}
        />
         */}
      </LayoutOne>
    </Fragment>
  );
};

ProductDetail.propTypes = {
  location: PropTypes.object,
  product: PropTypes.object
};



export default ProductDetail;
