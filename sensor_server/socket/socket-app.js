let publicSocket = null;

const configure = function (io) {
    if (!isConfigured())
        publicSocket = io;
};

const isConfigured = function () {
    return publicSocket != null;
};

const createRefreshResponse = function (refresh) {
    return {
        refresh: refresh
    };
};

const emitEvent = function (eventName, body) {
    publicSocket.emit(eventName, body);
};
// const notifyCowsData = function(token,data){
//     emitEvent('/topic/cows/'+token,data)
// }
const coba = function(data){
    emitEvent('/topic/coba',data)
}
module.exports = {
    configure,
    coba
}