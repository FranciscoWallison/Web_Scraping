import fs from "fs";

(async () => {
  const validar = "./top-new.json";
  const validar_new = "./top-data-new.json";

  let result = [];

  await fs.readFile(validar, "utf8", async (error, data) => {
    if (error) {
      // console.error('Erro ao ler o arquivo JSON:', error);
      return;
    }
    const jsonData = JSON.parse(data);

    for (let index = 0; index < jsonData.length; index++) {
      const dataItem = jsonData[index];

      if (dataItem.id === 0) {
        continue;
      }

      let novoTextoTOPO = "Topo";
      let novoTextoMEIO = "Meio";
      let novoTextoBAIXO = "Baixo";

      let textoTypo = dataItem.TypeItem;

      let new_object;

      if (typeof textoTypo === "object") {

        new_object = {
          id: dataItem.id,
          name: dataItem.name,
          viewID: dataItem.viewID,
          textoTypo: dataItem.TypeItem,
        };

      } else {

        const new_type = [];

        if (textoTypo.toLowerCase().includes(novoTextoTOPO.toLowerCase())) {
          new_type.push("TOPO");
        }

        if (textoTypo.toLowerCase().includes(novoTextoMEIO.toLowerCase())) {
          new_type.push("MEIO");
        }

        if (textoTypo.toLowerCase().includes(novoTextoBAIXO.toLowerCase())) {
          new_type.push("BAIXO");
        }

        new_object = {
          id: dataItem.id,
          name: dataItem.name,
          viewID: dataItem.viewID,
          textoTypo: new_type,
        };
      }

      result.push(new_object);
    }

    // Converte o objeto em uma string JSON
    const dadosJSON = JSON.stringify(result, null, 2);

    // Salva a string JSON em um arquivo
    fs.writeFile(validar_new, dadosJSON, "utf8", (err) => {
      if (err) {
        console.error("Erro ao salvar o arquivo JSON:", err);
      } else {
        console.log(`Arquivo JSON "${validar_new}" salvo com sucesso.`);
      }
    });
  });
})();
