import axios from 'axios';
import { atom, selector } from 'recoil';

export const GetProduct = async () => {
    //const setProduct = useSetRecoilState(productState);
    try {
        const {
            data: { results }
        } = await axios.get(`http://127.0.0.1:8000/api/v1/products/list`);
        //setProduct({product: results});
        
        return results;
    } catch (e) {
        console.warn(e);
        return [];
    }
}


export const productState = atom({
    key: 'product',
    default: {
        product: []
    }

});


export const productListSelector = selector({
    key: 'productList',
    get: async ({ get }) => {
        try {
            const {
                data: { results }
            } = await axios.get(`http://127.0.0.1:8000/api/v1/products/list`);
            //setProduct({product: results});
            
            return results;
        } catch (e) {
            console.warn(e);
            return [];
        }

    },
    set: ({ set }, newValue) => { 
        set(productState, newValue);
    }
 
});

