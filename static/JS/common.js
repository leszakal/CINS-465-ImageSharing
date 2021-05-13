function confirmDeletePost(id) {
  $('#deletePostModal').modal();
  $('#deleteButton').html('<input type="submit" class="btn btn-danger" onclick="return closeDeleteModal('+id+')" value="Delete"></input>');
}

function confirmDeleteComment(p_id, c_id) {
  $('#deleteCommentModal').modal();
  $('#deleteButtonCom').html('<form method="GET" action="/posts/'+p_id+'/comments/'+c_id+'/delete/"><input type="submit" name="delcom" class="btn btn-danger" onclick="return closeDeleteModal('+p_id+')" value="Delete"></input></form>');
}

function closeDeleteModal(id) {
  $('#deleteModal').modal('hide');
  return true
}
