// Default version (all methods)
import algoliasearch from 'algoliasearch';

// Search-only version
// import algoliasearch from 'algoliasearch/lite';

const client = algoliasearch('MXP1WFVWGE', '2eb8acc230f7fde7375935e999726a22');
const index = client.initIndex('mulbx_blog');

import indexJson from "./public/index.json" assert { type: "json" };

index.saveObjects(indexJson, {
    autoGenerateObjectIDIfNotExist: true
}).then(({ objectIDs }) => {
    console.log(objectIDs);
});